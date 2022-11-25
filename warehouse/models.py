from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=36)
    country = models.CharField(max_length=256)

    products = models.ManyToManyField("wood.Product", through='wood.Product_City')

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        return f"{self.name}:{self.code}"

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=36)
    map_url = models.ImageField(upload_to="maps", default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPIHJQ_j5byp-SD9Is88D6h-a72knRe_YS4Q&usqp=CAU")
    city_id = models.ForeignKey(City, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = 'Bodega'
        verbose_name_plural = 'Bodegas'

    def __str__(self):
        return f"{self.name}"

class Location(models.Model):
    name = models.CharField(max_length=100)
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = 'Ubicación'
        verbose_name_plural = 'Ubicaciones'

    def __str__(self):
        return f"{self.name}"