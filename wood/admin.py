from django.contrib import admin

from .models import Line, Inventory_Type, Product, Kit, Wood_State, Product_City

# Register your models here.

admin.site.register(Line)
admin.site.register(Inventory_Type)
admin.site.register(Product)
admin.site.register(Kit)
admin.site.register(Wood_State)
admin.site.register(Product_City)
