import datetime
from django.db import models

from warehouse.models import City
from django.utils import timezone

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=80)
    # for_user_id = models.ForeignKey(User, on_delete=models.CASCADE) # For future reference
    created_at = models.DateTimeField("Created datetime", auto_now_add=True)

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.name


class User(models.Model):
    # id 
    email = models.CharField(max_length=80)
    password = models.CharField(max_length=256)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    photo_url = models.CharField(max_length=256, null=True)
    document = models.CharField(max_length=20)
    charge = models.CharField(max_length=20, null=True)
    city_id = models.ForeignKey(City, on_delete=models.RESTRICT)
    role_id = models.ForeignKey(Role, on_delete=models.RESTRICT)
    active = models.BooleanField()
    created_at = models.DateTimeField("Created datetime", auto_now_add=True)
    updated_at = models.DateTimeField("Created datetime", auto_now_add=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)

class Employee(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    city_id = models.ForeignKey(City, on_delete=models.RESTRICT)
    nit = models.CharField(max_length=256)

    created_at = models.DateTimeField("Created datetime", auto_now_add=True)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Provider(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    city_id = models.ForeignKey(City, on_delete=models.RESTRICT)
    nit = models.CharField(max_length=256)

    created_at = models.DateTimeField("Created datetime", auto_now_add=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"