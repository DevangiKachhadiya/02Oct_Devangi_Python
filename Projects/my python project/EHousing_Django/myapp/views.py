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
    return render(request, 'log_in.html', {'msg':msg, "user": user})

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
                return redirect('/log_in')
            
        else:
            print(newuser.errors)
            msg = "Error! Somethings went wrong..."
    return render(request, 'signUp.html', {'msg': msg})

def add_homee(request):
    msg = ""
    errors = []
    
    if request.method == 'POST':
        form = addhomeForm(request.POST)
        images = request.FILES.getlist('image')

        # Form validation
        if form.is_valid():
            # Image Validation
            if not images:
                errors.append("Please upload at least one image.")
            elif len(images) > 10:
                errors.append("You can upload a maximum of 10 images.")
            else:
                for image in images:
                    if image.size > 5 * 1024 * 1024:  # 5MB limit
                        errors.append(f"Image {image.name} exceeds 5MB size limit.")
                    if not image.content_type.startswith('image/'):
                        errors.append(f"File {image.name} is not a valid image.")
            
            if not errors:
                home_instance = form.save()

                # Save images
                for image in images:
                    HomeImage.objects.create(home=home_instance, image=image)
                
                msg = 'Added home successfully with images'
            else:
                msg = 'Error in image upload. Please check the image files.'
        else:
            errors.extend(form.errors.values())
            msg = 'Form has errors. Please check the fields.'

    else:
        form = addhomeForm()

    return render(request, "add_homee.html", {'msg': msg, 'errors': errors, 'form': form})

def buy_home(request):
    return render(request, "buy_home.html")

def rent_home(request):
    return render(request, 'rent_home.html')

def show_home(request):
    return render(request, 'show_home.html')

def extra(request):
    return render(request, 'extra.html')

def latest_extra(request):
    return render(request, 'latest_extra.html')

def searchbar(request):
    return render(request, 'searchbar.html')

def slider_section(request):
    return render(request, 'slider_section.html')
