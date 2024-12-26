from django.shortcuts import render
from .forms import *

# Create your views here.

def index(request):
    if request.method=='POST':
        stdata=studData(request.POST)
        if stdata.is_valid():
            stdata.save()
            print("Data inserted successfully!")
        else:
            print(stdata.errors)
    return render(request,'index.html')

def showdata(request):
    sd=studinfo.objects.all()
    return render(request,'showdata.html',{'stdata':sd})