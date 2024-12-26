from django import forms
from .models import *

class santaData(forms.ModelForm):
    class Meta:
        model=Santa
        fields='__all__'

class loginData(forms.ModelForm):
    class Meta:
        model=Login
        fields='__all__'
