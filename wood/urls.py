from django.urls import path

from . import views 

urlpatterns = [
    path("get_settings", views.get_settings, name="get_settings"),
    path("kit/<int:kit_id>", views.readUpdateOrDelete, name="read_update_delete"),
    path("kit", views.listOrCreateKit, name="list_create"),
]