from django import forms
from .models import *

class productForm(forms.ModelForm):
    class Meta:
        model=product
        fields='__all__'

class subcateFrom(forms.ModelForm):
    class Meta:
        model=subcategory
        fields=['modelname','price']