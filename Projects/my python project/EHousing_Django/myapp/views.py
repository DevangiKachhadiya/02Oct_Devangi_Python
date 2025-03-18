from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth import logout
import requests


# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    msg = ""
    user = request.session.get("user")
    if request.method == 'POST':
        unm = request.POST["email"]
        password = request.POST['pas']

        user = userSignup.objects.filter(email=unm, pas=password)
        userid = userSignup.objects.get(email=unm)
        print("UserID:", userid.id)
        if user:
            print("Login Successfully!")
            request.session["user"]= unm # session
            request.session["userid"]=userid.id
            return redirect("/")
        else:
            print("Error! Login Faild...PLZ Try Again...")
            msg = "Error! Login Faild...PLZ Try Again..."
    return render(request, 'login.html', {'msg':msg, "user": user})

def signUp(request):
    msg = ''
    if request.method == "POST":
        newuser = signupForm(request.POST)
        email = ''
        if newuser.is_valid():
            # Username verification
            try :
                email = newuser.cleaned_data.get('email')
                userSignup.objects.get(email=email)
                print("Email is already exists!")
                msg = 'Email is already exists!'
            except userSignup.DoesNotExist:
                newuser.save()
                return redirect('/login')
            
        else:
            print(newuser.errors)
            msg = "Error! Somethings went wrong..."
    return render(request, 'signUp.html', {'msg': msg})