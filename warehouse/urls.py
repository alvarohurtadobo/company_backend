

from django.urls import path

from . import views

urlpatterns = [
    path("warehouse", views.listWarehouses, name="list_warehouses"), ]
