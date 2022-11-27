from django.contrib import admin
from .models import User, Role, Employee, Provider

class UserAdmin(admin.ModelAdmin):
    fields = ["first_name", "last_name", "email", "password",
              "photo_url", "document", "city_id", "role_id", "active"]
    list_display = ["first_name", "last_name",
                    "email", "city_id", "role_id", "active"]
    search_fields = ["first_name", "last_name"]
    # readonly_fields = ("id",)


class EmployeeAdmin(admin.ModelAdmin):
    fields = ["first_name", "last_name", "nit", "city_id"]
    list_display = ["first_name", "last_name", "city_id"]
    search_fields = ["first_name", "last_name"]


class ProviderAdmin(admin.ModelAdmin):
    fields = ["first_name", "last_name", "nit", "city_id"]
    list_display = ["first_name", "last_name", "city_id"]
    search_fields = ["first_name", "last_name"]


admin.site.register(User, UserAdmin)
admin.site.register(Role)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Provider, ProviderAdmin)