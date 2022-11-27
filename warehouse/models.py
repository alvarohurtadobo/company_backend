from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    code = models.CharField(max_length=36, verbose_name="Código")
    country = models.CharField(max_length=256, verbose_name="País")

    products = models.ManyToManyField("wood.Product", through='wood.Product_City')

    class Meta:
        verbose_name = '3.1 Ciudad'
        verbose_name_plural = '3.1 Ciudades'

    def __str__(self):
        return f"{self.name}:{self.code}"

class Warehouse(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    code = models.CharField(max_length=36, verbose_name="Código")
    map_url = models.ImageField(upload_to="media/maps/", default="media/maps/default.png", verbose_name="Mapa guía")
    city_id = models.ForeignKey(City, on_delete=models.RESTRICT, verbose_name="Ciudad")

    class Meta:
        verbose_name = '3.2 Bodega'
        verbose_name_plural = '3.2 Bodegas'

    def __str__(self):
        return f"{self.name}"

class Location(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.RESTRICT, verbose_name="Bodega")

    class Meta:
        verbose_name = '3.3 Ubicación'
        verbose_name_plural = '3.3 Ubicaciones'

    def __str__(self):
        return f"{self.name}"