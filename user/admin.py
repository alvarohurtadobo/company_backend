from django.contrib import admin
from .models import User, Role, Employee, Provider

# Register your models here.

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Employee)
admin.site.register(Provider)
