from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
    if request.method=='POST':
        s=santaData(request.POST)
        if s.is_valid():
            s.save()
            print("Data Inserted Successfully!")
        else:
            print(s.errors)
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        l=loginData(request.POST)
        if l.is_valid():
            l.save()
            print("Login Successfully")
        else:
            print(l.errors)
    return render(request,'login.html')