from django import forms
from .models import *

class productForm(forms.ModelForm):
    class Meta:
        model=product
        fields='__all__'

class subcategoryFrom(forms.ModelForm):
    class Meta:
        model=subcategory
        fields='__all__'