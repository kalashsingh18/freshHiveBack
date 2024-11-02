from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from .serializers import Createformserializer,Questionformserializer
from rest_framework.response import Response
from .import models
from rest_framework import generics
@api_view(["POST","GET"])
def createform(request,form_id=None):
    if request.method=="GET":
        print(dir(createform))
        print(form_id)
        
        form_by_id = models.createform.objects.filter(id=form_id).first()
        print(form_by_id)
        serializer = Createformserializer(form_by_id)
        return Response(serializer.data)
    if request.method=="POST":
        print(request.data)
        serializer=Createformserializer(data=request.data)
        if serializer.is_valid():
            print("here")
            serializer.save()
            return Response(serializer.data)
        else:
            print("hereee")
            return Response(serializer.data)
# @api_view(["POST"])
# def question(request):
#     if request.method=="POST":
#             serializer=Questionformserializer(data=request.data)
#             if serializer.is_valid():
#                  serializer.save()
#                  return Response(serializer.data)
class CreateQuestion(generics.CreateAPIView):
     queryset=models.Question.objects.all()
     serializer_class=Questionformserializer
question=CreateQuestion.as_view()
    
