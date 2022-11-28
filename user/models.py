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
        verbose_name = '1.2 Role'
        verbose_name_plural = '1.2 Roles'

    def __str__(self):
        return self.name


class User(models.Model):
    # id 
    email = models.CharField(max_length=80, verbose_name="Correo electrónico")
    password = models.CharField(max_length=256, verbose_name="Contraseña")
    first_name = models.CharField(max_length=256, verbose_name="Nombres")
    last_name = models.CharField(max_length=256, verbose_name="Apellidos")
    photo_url = models.ImageField(upload_to="profiles/", default="media/profiles/default.png", verbose_name="Foto de perfil")
    document = models.CharField(max_length=20, verbose_name="Documento", blank=True)
    city_id = models.ForeignKey(City, on_delete=models.RESTRICT, verbose_name="Ciudad")
    role_id = models.ForeignKey(Role, on_delete=models.RESTRICT, verbose_name="Rol")
    active = models.BooleanField(verbose_name="¿Activo?", default=True)
    created_at = models.DateTimeField("Created datetime", auto_now_add=True)
    updated_at = models.DateTimeField("Created datetime", auto_now_add=True)

    class Meta:
        verbose_name = '1.1 Usuario'
        verbose_name_plural = '1.1 Usuarios'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)

class Employee(models.Model):
    first_name = models.CharField(max_length=256, verbose_name="Nombres")
    last_name = models.CharField(max_length=256, verbose_name="Apellidos")
    city_id = models.ForeignKey(City, on_delete=models.RESTRICT, verbose_name="Ciudad")
    nit = models.CharField(max_length=256, verbose_name="NIT")

    created_at = models.DateTimeField("Created datetime", auto_now_add=True)

    class Meta:
        verbose_name = '1.3 Empleado'
        verbose_name_plural = '1.3 Empleados'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Provider(models.Model):
    first_name = models.CharField(max_length=256, verbose_name="Nombres")
    last_name = models.CharField(max_length=256, verbose_name="Apellidos")
    city_id = models.ForeignKey(City, on_delete=models.RESTRICT, verbose_name="Ciudad")
    nit = models.CharField(max_length=256, verbose_name="NIT")

    created_at = models.DateTimeField("Created datetime", auto_now_add=True)

    class Meta:
        verbose_name = '1.4 Proveedor'
        verbose_name_plural = '1.4 Proveedores'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"