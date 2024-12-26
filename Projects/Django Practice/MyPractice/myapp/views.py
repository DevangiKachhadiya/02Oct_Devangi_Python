from django.shortcuts import render
from .forms import *

# Create your views here.

def index(request):
    if request.method=='POST':
        emp=empdata(request.POST)
        if emp.is_valid():
            emp.save()
            print("Data Inserted Successfully!")
        else:
            print(emp.errors)
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')



