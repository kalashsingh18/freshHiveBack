from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from .serializers import Createformserializer,Questionformserializer,Choiceformserializer
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

class Createchoices(generics.CreateAPIView):
    queryset=models.Choice.objects.all() 
    serializer_class=Choiceformserializer
choice=Createchoices.as_view() 
question=CreateQuestion.as_view()
@api_view(["POST"])
def getForm(request):
    if request.method=="POST":
        if request.data:
            # id=request.data["id"]
            form=models.createform.objects.filter(id=1)
            formdata=form.values()
            print(formdata[0])
            questions=models.Question.objects.filter(form=formdata[0]["id"]).values()
            for question in questions:
                    if models.Choice.objects.filter(question=question["id"]).values():
                        question["choices"]=models.Choice.objects.filter(question=question["id"]).values()
            print(questions)
            return Response({"formdata":formdata,"questions":questions})

