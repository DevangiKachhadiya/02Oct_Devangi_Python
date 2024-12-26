from django import forms
from .models import *

class empdata(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'

