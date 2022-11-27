from django.db import models
# from django.utils import timezone
from warehouse.models import Location, City
from user.models import Provider, User, Employee

class Wood_State (models.Model):
    name = models.CharField(max_length=256, verbose_name="Nombre")

    class Meta:
        verbose_name = "2.5 Estado de madera"
        verbose_name_plural = "2.5 Estados de madera"

    def __str__(self):
        return self.name
    

class Line (models.Model):
    name = models.CharField(max_length=256, verbose_name="Nombre")
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)

    class Meta:
        verbose_name = "2.1 Línea"
        verbose_name_plural = "2.1 Líneas"

    def __str__(self):
        return self.name

class Inventory_Type (models.Model):
    name = models.CharField(max_length=256, verbose_name="Nombre")

    class Meta:
        verbose_name = "2.4 Tipo de inventario"
        verbose_name_plural = "2.4 Tipos de inventario"

    def __str__(self):
        return self.name

class Product (models.Model):
    name = models.CharField(max_length=256, verbose_name="Nombre")
    code = models.CharField(max_length=32, verbose_name="Código")
    inventory_type_id = models.ForeignKey(Inventory_Type, on_delete=models.PROTECT, verbose_name="Tipo de inventario")
    line_id = models.ForeignKey(Line, on_delete=models.PROTECT, verbose_name="Línea")

    is_wood = models.BooleanField(default=False, verbose_name="¿Es madera?")
    length = models.DecimalField(null=True, decimal_places=2, max_digits=8, verbose_name="Longitud", blank=True)
    width = models.DecimalField(null=True, decimal_places=2, max_digits=8, verbose_name="Ancho", blank=True) # TODO, en siguiente migración volver obligatorios con defecto 0
    height = models.DecimalField(null=True, decimal_places=2, max_digits=8, verbose_name="Alto", blank=True)
    species = models.CharField(max_length=256, null=True, verbose_name="Especie", blank=True)

    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("Fecha de creación", auto_now_add=True)

    class Meta:
        verbose_name = "2.2 Producto"
        verbose_name_plural = "2.2 Productos"

    def __str__(self):
        return self.code + ": " + self.name

class Kit (models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Producto")
    state_id = models.ForeignKey(Wood_State, on_delete=models.PROTECT, verbose_name="Estado")
    amount = models.IntegerField(default=0, verbose_name="Cantidad")
    #Location
    location_id = models.ForeignKey(Location, related_name="current", on_delete=models.PROTECT, verbose_name="Ubicación")
    destiny_location_id = models.ForeignKey(Location, related_name="destiny", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Ubicación de destino")
    original_location_id = models.ForeignKey(Location, related_name="original", on_delete=models.PROTECT, null=True, blank=True, verbose_name="Ubicación de origen")
    #Users # toas ondelte:
    external_provider_id = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Proveedor externo")
    employee_id = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Empleado")
    updating_user_id = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Usuario de última actualización")
    # Aux
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("Fecha de creación", auto_now_add=True)

    class Meta:
        verbose_name = "2.3 Kit"
        verbose_name_plural = "2.3 Kits"

    def __str__(self):
        return f"Id: {self.pk}"
    
    def productor_externo(self):
        return self.external_provider_id is not None # or ((self.employee_id is None) and (self.original_location_id is None))
    
class Product_City (models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Producto")
    city_id = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name="Ciudad con existencia de producto")
    class Meta:
        verbose_name = '2.6 Asignación de Producto a ciudad'
        verbose_name_plural = '2.6 Asignación de Productos a ciudades'

    def __str__(self):
        return f"{self.product_id.name} - {self.city_id.name}"