from django import forms
from django.forms import ModelForm
from .models import *

class Todoform(forms.ModelForm):
    class Meta:
        model=Todolist
        fields="__all__"

        
    

