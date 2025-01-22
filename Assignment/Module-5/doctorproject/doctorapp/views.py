from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import logout
# Create your views here.

def login(request):
    msg=""
    user=request.session.get("user")
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        user=registeration.objects.filter(username=unm,password=pas)
        userid=registeration.objects.get(username=unm)
        print("UserID:",userid.id)
        if user:
            print("Login Successfully!")
            msg="Login Successfully!"
            request.session['user']=unm
            request.session['userid']=userid.id
            return redirect('/')
        else:
            print('Error! Login Faild...')
            msg="Oops! Login Faild..."
    return render(request,'login.html',{'msg':msg,'user':user})

def registration(request):
    msg=""
    if request.method=='POST':
        newuser=registerForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Registration Successfully!")
            msg="Registration Successfully!"
            return redirect('/login')
        else:
            print(newuser.errors)
            msg="Oops! Something went wrong...!"
    return render(request,'registration.html',{'msg':msg})


def doctor_list(request):
    
    doctor_data=[
        {'name':'Dr.Devangi', 'specialization':'Gynaecologist','experience':18, 'contact':'0190221111'},
        {'name':'Dr.Vivek', 'specialization':'Cardiologist','experience':15, 'contact':'9123456320'},
        {'name':'Dr.Jeet', 'specialization':'Dentist','experience':10, 'contact':'8103210100'},
        {'name':'Dr.Bindiya', 'specialization':'Surgeon','experience':20, 'contact':'9000063121'},
        {'name':'Dr.Mayur', 'specialization':'Neurologist','experience':25, 'contact':'9413459000'},
        {'name':'Dr.Palak', 'specialization':'Family Doctor','experience':5, 'contact':'1234678901'},
    ]
    return render(request,'doctor_list.html',{'doctor':doctor_data})

def index(request):
    user=request.session.get('user')
    return render(request,'index.html',{'user':user})

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def blogdetails(request):
    return render(request,'blogdetails.html')

def contact(request):
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
    return render(request,'contact.html',{'msg':msg})

def doctors(request):
    msg=""
    if request.method=='POST':
        apptm=appointmentForm(request.POST)
        if apptm.is_valid():
            apptm.save()
            print("Your Appointment Has Been Submited!")
            msg="Your Appointment Has Been Submited!"
        else:
            print(apptm.errors)
            msg="Error! Something went Wrong...!"
    return render(request,'doctors.html',{'msg':msg})

def doctorprofile(request):
    msg=""
    if request.method=='POST':
        dp=doctorProfileForm(request.POST)
        if dp.is_valid():
            dp.save()
            print("Record Inserted Successfully!")
            msg="Record Inserted Successfully!"
        else:
            print(dp.errors)
            msg="Error! Something went Wrong...! Try Again "
    return render(request,'doctorprofile.html',{'msg':msg})

def userlogout(request):
    logout(request)
    return redirect('/')

def updatedata(request,id):
    updt=DoctorProfile.objects.get(id=id)
    print("Current ID:",updt)
    if request.method=='POST':
        updReq=updateData(request.POST,instance=updt)
        if updReq.is_valid():
            updReq.save()
            print("Update Record Successfully!")
            return redirect('showdata')
        else:
            print(updReq.errors)
    return render(request,'updatedata.html',{'updt':updt})

def showdata(request):
    updata=DoctorProfile.objects.all()
    return render(request,'showdata.html',{'updata':updata})

def deletedata(request,id):
    updt=DoctorProfile.objects.get(id=id)
    DoctorProfile.delete(updt)
    return redirect('showdata')
