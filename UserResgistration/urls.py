from django.contrib import admin
from django.urls import path
from .views import create_user,login_user
urlpatterns = [
   
    path("",create_user,name="user_creation"),
    path("login",login_user,name="user_creation"),
    
]