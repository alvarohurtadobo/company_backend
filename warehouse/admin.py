from django.contrib import admin
from .models import City, Warehouse, Location


class CityAdmin(admin.ModelAdmin):
    fileds = ["name", "code", "country"]
    list_display = ["name", "code", "country"]


class WarehouseAdmin(admin.ModelAdmin):
    fields = ["name", "code", "city_id", "map_url"]
    list_display = ["name", "code", "city_id"]


class LocationAdmin(admin.ModelAdmin):
    fields = ["name", "warehouse_id"]
    list_display = ["name", "warehouse_id"]


admin.site.register(City, CityAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(Location, LocationAdmin)
