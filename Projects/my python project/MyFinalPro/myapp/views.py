from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
import re
from django.contrib.auth import logout
from django.core.mail import send_mail
from MyFinalPro import settings

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    msg = ""
    user = request.session.get("user")
    if request.method == 'POST':
        unm = request.POST["email"]
        password = request.POST['password']
        user = UserSignUp.objects.filter(email=unm, password=password)
        userid = UserSignUp.objects.get(email=unm)
        print("UserID:", userid.id)
        if user:
            print("Login Successfully!")
            request.session["user"]= unm # session
            request.session["userid"]=userid.id
            return redirect("/")
        else:
            print("Error! Login Faild...PLZ Try Again...")
            msg = "Error! Login Faild...PLZ Try Again..."
    return render(request, 'login.html', {'msg': msg})

def signUp(request):
    msg = ''
    if request.method == "POST":
        newuser = signupForm(request.POST)
        email = ''
        if newuser.is_valid():
            # Username verification
            try :
                email = newuser.cleaned_data.get('email')
                UserSignUp.objects.get(email=email)
                print("Email is already exists!")
                msg = 'Email is already exists!'
            except UserSignUp.DoesNotExist:
                msg = "Account created successfully! Please log in."
                newuser.save()
                return redirect('/login')
            
        else:
            print(newuser.errors)
            msg = "There was an error in your form submission. Please check the highlighted fields."
    else:
        newuser = signupForm()       

    return render(request, 'signUp.html', {'msg': msg, 'newuser':newuser})


def add_home(request):
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

    return render(request, "add_home.html", {'msg': msg, 'errors': errors, 'form': form})


def buy_home(request):
    return render(request, 'buy_home.html')

def rent_home(request):
    return render(request, 'rent_home.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    msg = ''
    user=request.session.get("user")
    if request.method=="POST":
        newcontact=contactForm(request.POST)
        if newcontact.is_valid():
            newcontact.save()
            print("Your data has been submited!")
            msg = 'Your data has been submited!'

             # Email Sending Code
            send_mail(
                subject='Thank You for Contacting Us!',
                message=f"Hello User!\n\nWe appreciate your interest and look forward to assisting you.Thank you for reaching out to E-Housing. We’ve received your inquiry and will get back to you soon. If you need immediate assistance, please contact us at shivkali690@gmail.com\n\nThanks & Regards!\nE-Housing.\n+91 9876543210| shivkali690@gmail.com",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[request.POST['email']],
            )

        else:
            print(newcontact.errors)
            msg = 'Error! Plz try again'
    return render(request, 'contact_us.html',{'user':user,'msg':msg})

def reset_password(request):
    return render(request, 'reset_password.html')

def show_home(request):
    return render(request, 'show_home.html')

def page404(request):
    return render(request, 'page404.html')

def page500(request):
    return render(request, 'page500.html')


def userlogout(request):
    logout(request)
    return redirect('/')