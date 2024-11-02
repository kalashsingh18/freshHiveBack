from rest_framework.serializers import ModelSerializer
from .models import createform
class Createformserializer(ModelSerializer):
    class Meta:
       model=createform
       fields= "__all__"