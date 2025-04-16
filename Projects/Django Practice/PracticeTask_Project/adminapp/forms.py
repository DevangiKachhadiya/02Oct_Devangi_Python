from django import forms
from .models import *

class categoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class addProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class updateproductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price','stock','category','image']

