from django.contrib import admin
from django.urls import path
from .views import createform,question,choice,getForm
urlpatterns = [
   path("",createform,name="createform"),
   path("/<int:form_id>/",createform,name="createform"),
   path("/question",question,name="create_questions"),
   path("/choice",choice,name="create_questions"),
   path("/formdata",getForm,name="formdata")
]