from django.contrib import admin
from . import views
from django.urls import path, include 

urlpatterns = [
    path("login/", views.login_user, name="login"),
]
