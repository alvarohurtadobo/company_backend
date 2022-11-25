from django.urls import path

from . import views 

urlpatterns = [
    path("register", views.RegisterApi.as_view(), name="register"),
    path("login", views.login, name="login"),
    path("login_token", views.loginNoPassword, name="login_token"),
    path("employees", views.listEmployees, name="List employees"),
    path("providers", views.listProviders, name="List providers"),
]