from django.urls import path

from . import views 

urlpatterns = [
    path("get_settings", views.get_settings, name="get_settings"),
    path("kit/<int:kit_id>", views.readUpdateOrDelete, name="read_update_delete"),
    path("kit_expanded/<int:kit_id>", views.read_kit_expanded, name="read_kit_expanded"),
    path("kit", views.listOrCreateKit, name="list_create"),
    # path("search_kits/<int:product_id>/<int:wood_state_id>/<int:location_id>", views.listOrCreateKit, name="list_create"),
    path("search_kits", views.searchKits, name="search"),
    path("products_by_city/<int:city_id>", views.list_products_by_city, name="list_products_by_city")
]