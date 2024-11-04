from rest_framework.serializers import ModelSerializer
from .models import createform,Question,Choice
class Createformserializer(ModelSerializer):
    class Meta:
       model=createform
       fields= "__all__"
class Questionformserializer(ModelSerializer):
    class Meta:
        model=Question
        fields="__all__"
class Choiceformserializer(ModelSerializer):
    class Meta:
        model=Choice
        fields="__all__"