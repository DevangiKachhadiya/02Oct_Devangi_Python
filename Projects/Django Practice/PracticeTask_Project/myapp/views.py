from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .forms import *
from adminapp.models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
    user = request.session.get('user')
    vc = Category.objects.all()
    return render(request, 'home.html',{'user':user, 'vc':vc})

def login(request):
    if request.method == 'POST':

        email = request.POST['email']
        pas = request.POST['password']

        user = UserSignUp.objects.filter(email=email, password=pas).first()
        if user:
            print('Login Successfully')
            request.session['user'] =user.email
            return redirect('/home')
        else:
            print("Login Failed")
    return render(request,'login.html')

def signUp(request):
    if request.method == 'POST':
        newuser = UserSigUpForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            return redirect('/login')
        else:
            print(newuser.errors)
    return render(request,'signUp.html')

def reqProduct(request):
    user_email = request.session.get('user')
    cat = Category.objects.all()

    if not user_email:
        return redirect('login')  # make sure user is logged in

    if request.method == "POST":
        rp = ReqProductForm(request.POST, request.FILES)
        if rp.is_valid():
            pro = rp.save(commit=False)
            user_obj = UserSignUp.objects.filter(email=user_email).first()
            if user_obj:
                pro.user = user_obj
                pro.save()
                return redirect('requestedProducts')
            else:
                return HttpResponse("User not found", status=404)
        else:
            print(rp.errors)

    return render(request, 'reqProduct.html', {'cat': cat})


def vpro(request):
    vp = Product.objects.all()
    ap = ReqProduct.objects.filter(status='approved')
    return render(request, 'vpro.html', {'vp':vp, 'ap':ap})