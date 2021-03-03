
from rest_framework import serializers
from .models import *
class Serializer(serializers.ModelSerializer):
    class Meta:
        model=Todolist
        fields="__all__"

        
    

