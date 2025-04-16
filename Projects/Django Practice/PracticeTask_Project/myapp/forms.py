from django import forms
from .models import *

class UserSigUpForm(forms.ModelForm):
    class Meta:
        model = UserSignUp
        fields = '__all__' 

class ReqProductForm(forms.ModelForm):
    class Meta:
        model = ReqProduct
        fields = ['name','price','stock','image','category']