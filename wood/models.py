from django.db import models
# from django.utils import timezone
from warehouse.models import Location, City
from user.models import Provider, User, Employee

class Wood_State (models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Estado de madera"
        verbose_name_plural = "Estados de madera"

    def __str__(self):
        return self.name
    

class Line (models.Model):
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)

    class Meta:
        verbose_name = "Familia"
        verbose_name_plural = "Familias"

    def __str__(self):
        return self.name

class Inventory_Type (models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = "Tipo de inventario"
        verbose_name_plural = "Tipos de inventario"

    def __str__(self):
        return self.name

class Product (models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=32)
    inventory_type_id = models.ForeignKey(Inventory_Type, on_delete=models.PROTECT)
    line_id = models.ForeignKey(Line, on_delete=models.PROTECT)

    is_wood = models.BooleanField(default=False)
    length = models.DecimalField(null=True, decimal_places=2, max_digits=8)
    width = models.DecimalField(null=True, decimal_places=2, max_digits=8) # TODO, en siguiente migración volver obligatorios con defecto 0
    height = models.DecimalField(null=True, decimal_places=2, max_digits=8)
    species = models.CharField(max_length=256, null=True)

    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("Fecha de creación", auto_now_add=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.code + ": " + self.name

class Kit (models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    state_id = models.ForeignKey(Wood_State, on_delete=models.PROTECT)
    amount = models.IntegerField(default=0)
    #Location
    location_id = models.ForeignKey(Location, related_name="current", on_delete=models.PROTECT)
    destiny_location_id = models.ForeignKey(Location, related_name="destiny", on_delete=models.SET_NULL, null=True)
    original_location_id = models.ForeignKey(Location, related_name="original", on_delete=models.PROTECT, null=True)
    #Users # toas ondelte:
    external_provider_id = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    updating_user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    # Aux
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    updated_at = models.DateTimeField("Fecha de creación", auto_now_add=True)

    class Meta:
        verbose_name = "Kit"
        verbose_name_plural = "Kits"

    def __str__(self):
        return "Id: "+self.pk
    
class Product_City (models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    city_id = models.ForeignKey(City, on_delete=models.PROTECT)
    class Meta:
        verbose_name = 'Asignación'
        verbose_name_plural = 'Asignaciones'

    def __str__(self):
        return f"{self.name}:{self.code}"