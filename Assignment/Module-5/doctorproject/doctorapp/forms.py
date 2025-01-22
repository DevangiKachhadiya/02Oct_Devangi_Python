from django import forms
from .models import *

class registerForm(forms.ModelForm):
    class Meta:
        model=registeration
        fields='__all__'

class appointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields='__all__'

class doctorProfileForm(forms.ModelForm):
    class Meta:
        model=DoctorProfile
        fields='__all__'

class contactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'

class updateData(forms.ModelForm):
    class Meta:
        model=DoctorProfile
        fields=['firstname','lastname','opt','username','city','password','mobile']