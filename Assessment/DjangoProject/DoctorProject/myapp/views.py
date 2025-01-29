from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth import logout

# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

def base(request):
    return render(request,'base.html')

def Appointment(request):
    return render(request,'Appointment.html')

def patient(request):
    return render(request,'patient.html')

def doctor(request):
    return render(request,'doctor.html')

def contact(request):
    msg=""
    if request.method=='POST':
        cn=contactForm(request.POST)
        if cn.is_valid():
            cn.save()
            print("Record Inserted Successfully!")
            msg="Record Inserted Successfully!"
        else:
            print(cn.errors)
            msg="Error! Something went Wrong...!"

    return render(request,'contact.html',{'msg':msg})

