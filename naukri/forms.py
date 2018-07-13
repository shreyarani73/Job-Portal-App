from django import forms
from .models import *

class Seekernewuserform(forms.ModelForm):
    class Meta:
        model= Seeker
        fields= ["s_name", 
        "email", 
        "contactno", 
        "skills"]
