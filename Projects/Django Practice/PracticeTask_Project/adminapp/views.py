from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout
from myapp.models import *
from django.utils.timezone import now
from django.contrib import messages

# Create your views here.

def dashboard(request):
    total_category = Category.objects.count()
    total_product = Product.objects.count()
    rcp = ReqProduct.objects.count()
    tcp = total_product + rcp
    return render(request, 'dashboard.html',{'tcp':tcp,'total_category':total_category})

def adminlogin(request):
    if request.method == 'POST':
        email= request.POST['email']
        password = request.POST['password']

        if email == 'admin@gmail.com' and password == 'admin':
            print('Login succesfully!')
            return redirect('/dashboard')
        else:
            print('Login failed! Something went wrong...')

    return render(request,'adminlogin.html')

def addCategory(request):
    if request.method == 'POST':
        cat=categoryForm(request.POST)
        if cat.is_valid():
            cat.save()
            print('category added successfully!')
            return redirect('/dashboard')
        else:
            print(cat.errors)
    return render(request, 'addCategory.html')

def addProduct(request):
    cat = Category.objects.all()
    print(Category.objects.all())

    if request.method == 'POST':
        newprod = addProductForm(request.POST, request.FILES)
        if newprod.is_valid():
            newprod.save()
            print("New Product Added!")
            return redirect('/dashboard')
        else:
            print(newprod.errors)
    return render(request, 'addProduct.html',{'cat':cat}) 

def viewProducts(request):
    vp = Product.objects.all()
    ap = ReqProduct.objects.filter(status='approved')
    return render(request, 'viewProducts.html', {'vp':vp, 'ap':ap})

def editProduct(request,id):
    user = request.session.get('user')
    userid = request.session.get('userid')
    categories = Category.objects.all()
    upid = Product.objects.get(id=id)
    print("Current User ID:",upid)
    if request.method == 'POST':
        if 'image' in request.FILES:
            upid.image = request.FILES['image']
            upid.save()
            return redirect('viewProducts') 
    updReq = updateproductForm(request.POST, instance=upid)
    if updReq.is_valid():
        updReq.save()
        return redirect('/viewProducts')
    else:
        print(updReq.errors)
    return render(request, 'editProduct.html', {'user':user, 'upid':upid, 'userid':userid, 'categories':categories})

def deleteProduct(request, id):
    dpid = Product.objects.get(id=id)
    Product.delete(dpid)
    return redirect('viewProducts')

def viewCategories(request):
    cat = Category.objects.all()
    return render(request, 'viewCategories.html', {'cat':cat})

def requestedProducts(request):
    rp = ReqProduct.objects.filter(status='pending')
    return render(request,'requestedProducts.html',{'rp':rp})

def approveProduct(request, id):
    product = ReqProduct.objects.get(id=id)
    product.approved_at = now()
    product.status='approved'
    product.save()
    messages.success(request, f"'{product.name}' approved successfully.")
    print("Your Product Approved Successfully!")
    return redirect('requestedProducts')

def rejectProduct(request, id):
    product = ReqProduct.objects.get(id=id)
    product_name = product.name
    product.status='approved'
    product.delete()
    messages.warning(request, f"'{product_name}' rejected and deleted.")
    print("Your Product Rejected!Try again...")
    return redirect('requestedProducts')

def userlogout(request):
    logout(request)
    return redirect('/')