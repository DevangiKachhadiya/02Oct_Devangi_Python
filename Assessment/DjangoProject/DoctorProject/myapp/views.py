from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.core.mail import send_mail
from DoctorProject import settings
from django.contrib.auth import logout
import random

# Create your views here.

def index(request):
    user = request.session.get('user')
    return render(request,'index.html', {'user':user})

def signup(request):
    user = request.session.get('user')
    msg=""
    if request.method == "POST":
        newuser = signupForm(request.POST)
        if newuser.is_valid():

            #OTP Email Sending
            global otp
            otp = random.randint(111111, 999999)
            
            sub = "YOUR ONE TIME PASSWORD!"
            msg = f"Hello User! \n\n Your Registration is Confirm!:) \n\n Thanks for registration/Connecting with us!\n\n Thanks & Regards! \nHealthify:) "
            from_email = settings.EMAIL_HOST_USER
            to_email = [request.POST["email"]]

            send_mail(
                subject=sub, message=msg, from_email=from_email, recipient_list=to_email
            )
            newuser.save()
            return redirect("/login")
        else:
            print(newuser.errors)
            msg = "Error! Something Went Wrong"
    return render(request,'signup.html',{'msg':msg, 'user':user})

# def otpverify(request):
#     user = request.session.get('user')
#     msg = ""

#     #USE Session to store OTP instead of a global variable

#     if request.method == "POST":
#         if request.POST['otp'] == str(otp): 
#             print("Verification Done!")
#             return redirect("/")
#         else:
#             print("Error! Invalid OTP")
#             msg = "Error! Invalid OTP"
#     return render(request, 'otpverify.html', {'msg':msg, 'user':user})

def login(request):
    user = request.session.get('user')
    msg = ""

    if request.method == 'POST':
        # Retrieve form data
        role = request.POST.get('role') 
        email = request.POST.get('email') 
        password = request.POST.get('password') 
        
        # Validate input
        if not email or not password or not role:
            msg = "All fields are required."
        else:
            # Authenticate user
            user = Usersignup.objects.filter(email=email, password=password, role=role).first()
            if user:
                # Store user details in the session
                request.session['user'] = user.email
                request.session['role'] = user.role
                
                # Redirect based on role
                if user.role == 'Admin':
                    return redirect('/adminn')
                elif user.role == 'Doctor':
                    return redirect('/doctor')
                elif user.role == 'Patient':
                    return redirect('/patient')
                else:
                    msg = "Invalid role."
            else:
                msg = "Invalid credentials. Please try again."

    return render(request, 'login.html', {'msg': msg, 'user':user})


def base(request):
    user = request.session.get('user')
    return render(request,'base.html', {'user':user})

def Appointment(request):
    user = request.session.get('user')
    msg = ""
    if request.method == 'POST':
        ap = appointmentForm(request.POST)
        if ap.is_valid():
            ap.save()
            print("Your Appointment has been Booked Successfully!")
            msg = "Your Appointment has been Booked Successfully!"
            return redirect("patient")
        else:
            msg = "Opps! Something went Wrong!!!"
            print(ap.errors)
    return render(request,'Appointment.html', {'user':user ,'msg':msg})

def showapp(request):
    shApp = Appoi.objects.all()
    return render(request, 'showapp.html',{'shApp':shApp})

def deleteapp(request,id):
    said=Appoi.objects.get(id=id)
    Appoi.delete(said)
    return redirect('showapp')

def patient(request):
    user = request.session.get('user')
    return render(request,'patient.html', {'user':user})

def doctor(request):
    user = request.session.get('user')
    return render(request,'doctor.html', {'user':user})

def adddoctor(request):
    user = request.session.get('user')
    msg=""
    if request.method=='POST':
        ad=doctorsForm(request.POST, request.FILES)
        if ad.is_valid():
            ad.save()
            print("Record Inserted Successfully!")
            msg="Record Inserted Successfully!"
            return redirect('/showdoctors')
        else:
            print(ad.errors)
            msg="Error! Something went Wrong..  Please try again!"
    return render(request,'adddoctor.html',{'msg':msg, 'user':user})

def showdoctors(request):
    user = request.session.get('user')
    sd=Doctors.objects.all()
    return render(request, 'showdoctors.html',{'sd':sd, 'user':user})


def contact(request):
    user = request.session.get('user')

    msg=""
    if request.method=='POST':
        cn=contactForm(request.POST)
        if cn.is_valid():
            cn.save()
            print("Record Inserted Successfully!")
            msg="Record Inserted Successfully!"
        else:
            print(cn.errors)
            msg="Error! Something went Wrong...!"

    return render(request,'contact.html',{'msg':msg, 'user':user})

def about(request):
    user = request.session.get('user')
    return render(request,'about.html', {'user':user})

# def admindash(request):
#     user = request.session.get('user')
#     return render(request, 'dashboard.html', {'user':user})


# def deldoctdata(request,id):
#     user = request.session.get('user')

#     drid=Doctor.objects.get(id=id)
#     Doctor.delete(drid)
#     return redirect('showdoctdata', {'user':user})

def profile(request):
    user = request.session.get("user")
    urole = request.session.get("role")
    uid = Usersignup.objects.filter(role=urole,email=user).first()
    print("Current User ID:", uid)
    if request.method == "POST":
        updReq = updateForm(request.POST,instance=uid)
        if updReq.is_valid():
            updReq.save()
            request.session.delete()
            return redirect("/")
        else:
            print(updReq.errors)
            msg = "Error!Something went wrong...!"
    return render(request,'profile.html', {"user":user, "uid": uid})

def userlogout(request):
    logout(request)
    return redirect("/")

def forgotpass(request):
    user = request.session.get('user')
    urole = request.session.get('role')

    fp = Usersignup.objects.filter(role = urole, email = user).first()
    print("Current ID: ",fp)
    if request.method=='POST':
        upas = fpass(request.POST, instance = fp)
        if upas.is_valid():
            upas.save()
            print("Password Changed Successfully")
            msg = "Password Changed Successfully!"
            return redirect('/')
        else:
            print(upas.errors)
            msg = "Error! Something went Wrong... Please try again"

    return render(request, 'forgotpass.html', {'user': user, 'fp':fp})

def adminn(request):
    user = request.session.get('user')
    return render(request, 'adminn.html', {'user':user})