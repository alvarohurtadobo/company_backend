from django.contrib import admin
from .models import City, Warehouse, Location

# Register your models here.

admin.site.register(City)
admin.site.register(Warehouse)
admin.site.register(Location)
