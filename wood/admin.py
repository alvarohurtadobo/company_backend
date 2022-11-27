from django.contrib import admin

from .models import Line, Inventory_Type, Product, Kit, Wood_State, Product_City


class KitAdmin(admin.ModelAdmin):
    fields = ["product_id", "location_id", "state_id", "amount", "original_location_id",
              "employee_id", "external_provider_id", "updating_user_id"]  # ,"destiny_location_id"
    readonly_fields = ("created_at",)
    list_display = ["__str__", "product_id", "location_id",
                    "state_id", "amount", "productor_externo"]
    search_fields = ["product_id__name"]
    list_filter = ["created_at", "product_id", "location_id", "state_id"]


class ProductAdmin(admin.ModelAdmin):
    fields = ["code", "name", "inventory_type_id",
                "line_id", "is_wood", "length", "width", "height"]
    list_display = ["code", "name", "inventory_type_id", "line_id", "is_wood"]
    list_filter = ["created_at"]
    search_fields = ["code", "name"]

class ProductCityAdmin(admin.ModelAdmin):
    list_display = ["product_id", "city_id"]
    list_filter = ["city_id"]


admin.site.register(Line)
admin.site.register(Inventory_Type)
admin.site.register(Product, ProductAdmin)
admin.site.register(Kit, KitAdmin)
admin.site.register(Wood_State)
admin.site.register(Product_City, ProductCityAdmin)

