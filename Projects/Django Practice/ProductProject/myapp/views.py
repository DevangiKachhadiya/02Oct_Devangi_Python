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
            return redirect('/subcategorys')
        else:
            print(pro.errors)
            print("Opps! Something went Wrong...!")
            msg="Opps! Something went Wrong...!"

    return render(request,'products.html',{'msg':msg})

def subcategorys(request):
    msg=''
    if request.method=='POST':
        subcat=subcateFrom(request.POST)
        if subcat.is_valid():
            subcat.save()
            print("Data Added Successfully!")
            msg='Data Added Successfully!'
            return redirect('/')
        else:
            print(subcat.errors)
            msg='Opps! Something went wrong!'

    else:
        subcat=subcateFrom()
    return render(request,'subcategorys.html',{'msg':msg, 'form':subcat})