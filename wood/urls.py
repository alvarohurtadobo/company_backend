from django.urls import path

from . import views 

urlpatterns = [
    path("get_settings", views.get_settings, name="get_settings"),
]