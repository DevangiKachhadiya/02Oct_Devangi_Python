from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model = usersignup
        fields = "__all__"

class updateForm(forms.ModelForm):
    class Meta:
        model = usersignup
        fields = ["username","email","pwd","cpwd","contact"]

class contactForm(forms.ModelForm):
    class Meta:
        model = contactUs
        fields = "__all__"

class houseForm(forms.ModelForm):
    class Meta:
        model = house
        fields = ['title','property_type','listing_type','price','address','area','bedrooms','bathrooms','floors','main_image']

class HouseImageForm(forms.ModelForm):
    class Meta:
        model = HouseImage
        fields = ['image']

class complaintsForm(forms.ModelForm):
    class Meta:
        model = complaints
        fields = '__all__'
        