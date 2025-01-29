from django.shortcuts import render,redirect
from .forms import *
from .models import *


# Create your views here.

def index(request):
    return render(request,'index.html')

def products(request):
    msg=""
    if request.method=='POST':
        pro=productForm(request.POST)
        if pro.is_valid():
            pro.save()
            print("Data Added Successfully!")
            msg="Data Added Successfully!"
            return redirect('/subcategory')
        else:
            print(pro.errors)
            print("Opps! Something went Wrong...!")
            msg="Opps! Something went Wrong...!"

    return render(request,'products.html',{'msg':msg})

def subcategory(request):
    msg=""
    if request.method=='POST':
        subcat=subcategoryFrom(request.POST)
        if subcat.is_valid():
            subcat.save()
            print("Data Added Successfully!")
            msg="Data Added Successfully!"
            return redirect('/')
        else:
            print(subcat.errors)
            print("Opps! Something went Wrong...!")
            msg="Opps! Something went Wrong...!"

    return render(request,'subcategory.html',{'msg':msg})
    
