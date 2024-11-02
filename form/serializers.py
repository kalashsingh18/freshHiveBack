from rest_framework.serializers import ModelSerializer
from .models import createform,Question
class Createformserializer(ModelSerializer):
    class Meta:
       model=createform
       fields= "__all__"
class Questionformserializer(ModelSerializer):
    class Meta:
        model=Question
        fields="__all__"