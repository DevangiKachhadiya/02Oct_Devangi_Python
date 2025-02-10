from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model=Usersignup
        fields='__all__'

class updateForm(forms.ModelForm):
    class Meta:
        model = Usersignup
        fields = [
            "firstname",
            "email",
            "password",
            "contact",
        ]

class contactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'

class appointmentForm(forms.ModelForm):
    class Meta:
        model=Appoi
        fields='__all__'

class doctorsForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields= ['img', 'name', 'specialization', 'contact', 'address'] 

class fpass(forms.ModelForm):
    class Meta:
        model = Usersignup
        fields = ['password']