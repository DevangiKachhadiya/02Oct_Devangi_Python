from django.shortcuts import render, redirect
from .forms import *
from .models import *
from EHousing import settings
from django.core.mail import send_mail
from django.contrib.auth import logout

# Create your views here.

def index(request):
    user = request.session.get("user")
    return render(request, 'index.html', {"user":user})

def about(request):
    user = request.session.get("user")
    return render(request,'about.html', {"user":user})

def gallery(request):
    user = request.session.get("user")
    return render(request, 'gallery.html', {"user":user})

def contact(request):
    msg = ""
    user = request.session.get("user")
    if request.method == "POST":
        newcontact = contactForm(request.POST)
        if newcontact.is_valid():
            newcontact.save()
            print("Your data has been submited!")
            msg = "Your data has been submited!"

            # Email Sending Code
            send_mail(
                subject="Thankyou!",
                message=f"Hello User!\n\nThank you for connecting with us!\nWe will contact you.\n\nThanks & Regards!\nShivkali\n+91 9724000009 | shivkali690@gmail.com",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[request.POST['email']],
            )
        else:
            print(newcontact.errors)
            msg = "Opps! Something went wrong!"
    return render(request, 'contact.html', {"user":user , "msg":msg})

def properties(request):
    user = request.session.get("user")
    return render(request, 'properties.html',{'user':user})

def service(request):
    user = request.session.get("user")
    return render(request, 'service.html', {'user':user})

def login(request):
    msg = ""
    user = request.session.get("user")
    if request.method == "POST":
        unm = request.POST["email"]
        pas = request.POST["pwd"]

        user = usersignup.objects.filter(email=unm, pwd=pas)
        userid = usersignup.objects.get(email=unm)
        print("UserID:", userid.id)
        if user: #TRUE
            print("Login Successfull!")
            msg = "Login Successfully!"
            request.session["user"] = unm #session
            request.session["userid"] = userid.id
            return redirect("/")
        else:
            print("Error!Login Faild! Please try again...")
            msg = "Error!Login Faild! Please try again..."

    return render(request, 'login.html',{"msg":msg, "user":user})

def signup(request):
    msg = ""
    if request.method == 'POST':
       us = signupForm(request.POST)
       if us.is_valid():
           us.save()
           print("Registration Successfully!")
           msg = "Registration Successfully!"
           return redirect("/")
       else:
           print(us.errors)
           msg = "Error! Something went wrong..."
        
    return render(request, 'signup.html', {"msg":msg})

def updprofile(request):
    uid=request.session.get('userid')
    print("Cuurrnet ID:",uid)
    myid=usersignup.objects.get(id=uid)
    if request.method == 'POST':
        updreq = updateForm(request.POST,instance=myid)
        if updreq.is_valid():
           updreq.save()
           print("Profile Updated!")
           return redirect("/")
        else:
            print(updreq.errors)
    return render(request,'updprofile.html',{'myid':myid}) 

def userlogout(request):
    logout(request)
    return redirect("/")

def addhouse(request):
    user = request.session.get("user")
    msg = ""

    if request.method == 'POST':
        im = houseForm(request.POST, request.FILES) # handle text fields only
        images = request.FILES.getlist('images') # get multiple uploaded images

        print("FILES RE CEIVED:", images)

        if im.is_valid():
            house_instance = im.save()

            for i in images:
                HouseImage.objects.create(house=house_instance, image=i)

            msg = "House Added Successfully!"
            print(HouseImage.objects.all())
            return redirect('showhome')

        else:
            msg = "Error! Oops, something went wrong!"
            print(im.errors)
    else:
        im = houseForm()

    return render(request, 'addhouse.html', {'form': im, 'msg': msg, "user":user})


def complaints(request):
    if request.method == 'POST':
        compl = complaintsForm(request.POST)
        
    return render(request, 'complaints.html')


# def showhome(request):
#     shome = house.objects.all()
#     return render(request, 'showhome.html', {'shome':shome})

def showhome(request):
    shome = house.objects.prefetch_related('images').all()
    print(house.main_image)  # Check if main_image exists
    #print(house.images.all())  # Check if related images exist
    return render(request, 'showhome.html', {'shome':shome})
