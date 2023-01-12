import csv
from django.contrib import admin
from django.http import HttpResponse
from .models import Line, Inventory_Type, Product, Kit, Wood_State, Product_City, KitFollowup



class KitFollowupAdmin(admin.ModelAdmin):
    fields = ["kit_id", "product_id", "location_id", "state_id", "amount", "original_location_id",
              "employee_id", "external_provider_id", "updating_user_id", "used_at_datetime",
              "transformed_at_datetime", "source_kit_id"]  # ,"destiny_location_id"
    readonly_fields = ("created_at",)
    list_display = ["__str__", "kit_id", "product_id", "location_id",
                    "state_id", "amount", "productor_externo", "source_kit_id", "bodega", "linea", "created_at"]
    search_fields = ["product_id__name"]
    list_filter = ["kit_id", "product_id", "location_id"]
    actions = []

    def linea(self, obj):
        return getattr(getattr(obj, "product_id"), "line_id")
    
    def bodega(self, obj):
        return getattr(getattr(obj, "location_id"), "warehouse_id")
class KitAdmin(admin.ModelAdmin):
    fields = ["product_id", "location_id", "state_id", "amount", "original_location_id",
              "employee_id", "external_provider_id", "updating_user_id", "used_at_datetime",
              "transformed_at_datetime", "source_kit_id"]  # ,"destiny_location_id"
    readonly_fields = ("created_at",)
    list_display = ["__str__", "product_id", "location_id",
                    "state_id", "amount", "productor_externo", "source_kit_id", "bodega", "linea", "created_at"]
    search_fields = ["product_id__name"]
    list_filter = ["created_at", "product_id", "location_id", "state_id"]
    actions = ['export_as_csv']

    def linea(self, obj):
        return getattr(getattr(obj, "product_id"), "line_id")
    
    def bodega(self, obj):
        return getattr(getattr(obj, "location_id"), "warehouse_id")

    def export_as_csv(self, request, queryset):
        meta = self.model._meta 
        field_names = [field.name for field in meta.fields]
        extended_field_names =  [   "ID",
                                    "Producto", 
                                    "Estado",
                                    "Cantidad",
                                    "Ubicación",
                                    "Ubicación destino",
                                    "Lugar de creación", 
                                    "Proveedor externo", 
                                    "Empleado",
                                    "Usuario que actualiza",
                                    "Fecha de utilización",
                                    "Fecha de transformación",
                                    "Kit fuente",
                                    "Bodega", 
                                    "Línea",
                                    "Fecha de creación"]

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(extended_field_names)
        for obj in queryset:
            new_row = [getattr(obj, field) for field in field_names]
            # For line
            product = getattr(obj, "product_id")
            location = getattr(obj, "location_id")
            line_name =  getattr(product, "line_id")
            warehouse_name =  getattr(location, "warehouse_id")
            new_row = new_row[:-2] + [warehouse_name, line_name] + new_row[-2:-1]
            row = writer.writerow(new_row)
        return response

    export_as_csv.short_description = "Exportar como CSV"


class ProductAdmin(admin.ModelAdmin):
    fields = ["code", "name", "inventory_type_id",
              "line_id", "is_wood", "length", "width", "height", "species"]
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
admin.site.register(KitFollowup, KitFollowupAdmin)
