from django.shortcuts import render,redirect
from .import models
from rest_framework import response
import jwt
from datetime import datetime, timedelta
from .serializer import Userserializer
from rest_framework import generics
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
SECRET_KEY = "my_secret_key"

def generate_jwt_token(username):
    payload = {
        "username": username,
        "exp": datetime.utcnow() + timedelta(hours=1),  # Token expiration time
        "iat": datetime.utcnow(),                       # Issued at time
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token
def generate_refresh_token(username):
    payload = {
        "username": username,
        "exp": datetime.utcnow() + timedelta(days=7),  # Refresh token expires in 7 days
        "iat": datetime.utcnow(),
    }
    refresh_token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return refresh_token
@api_view(["POST"])
def create_user(request):
    if request.method=="POST":
        if request.data:
            unhashed_pass=request.data["password"]
            hashed_password=make_password(unhashed_pass)
            data=request.data
            data["password"]=hashed_password
            serializer=Userserializer(data=data)
            if serializer.is_valid():
                serializer.save()
                print(data)
                token=generate_jwt_token(data["full_name"])
                refresh_token=generate_refresh_token(username=data["full_name"])
                return response.Response({"token":token,"refresh_token":refresh_token})
@api_view(["POST"])
def login_user(request):
    
    if request.data:
        print(123)
        password=request.data["password"]
        
        
        print(request.data["username"])
        user=models.User.objects.filter(full_name=request.data["username"]).values()[0]
        print(user)
        check=check_password(password,user["password"])
        print(check)
        if check:
            token=generate_jwt_token(user["full_name"])
            refresh_token=generate_refresh_token(user["full_name"])
            tokens={"token":token,"refresh_token":refresh_token}
            return response.Response(tokens)







            


