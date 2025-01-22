from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout
from django.core.mail import send_mail
from FinalProject import settings

# Create your views here.

def index(request):
    msg=""
    user=request.session.get('user')
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        user=userSignup.objects.filter(username=unm,password=pas)
        userid=userSignup.objects.get(username=unm)
        print("UserID:",userid.id)

        if user: #True
            print("Login Successfull!")
            request.session['user']=unm #Session
            request.session['userid']=userid.id
            return redirect('Notes')
        else:
            print("Error! Login faild...! Try again...")
            msg="Error! Login faild...! Try again..."

    return render(request,'index.html',{'msg':msg,'user':user})

def signup(request):
    msg=""
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            return redirect('/')
        else:
            print(newuser.errors)
            msg="Error! Something Went Wrong"
    return render(request,'signup.html',{'msg':msg})


def Notes(request):
    msg=""
    user=request.session.get('user')
    userid=request.session.get('userid')
    username= ''

    if userid and userSignup.objects.filter(id=userid).exists():
        username=userSignup.objects.get(id=userid).username
        print("Username fetched: ",username)
    else:
        print("User Id not found or invalid!")
    
    if request.method=='POST':
        newnote=notesForm(request.POST,request.FILES)
        if newnote.is_valid():
            newnote.save()
            print("Your notes has been submitted!")
            msg="Your notes has been submitted!"
        else:
            print(newnote.errors)
            msg="Error! Something Went Wrong..."
            
    return render(request,'Notes.html',{'user':user,'msg':msg, 'username': username})

def Profile(request):
    user=request.session.get('user')
    userid=request.session.get('userid')
    cid=userSignup.objects.get(id=userid)
    print("Current User ID:",cid)
    if request.method=='POST':
        updateReq=updateForm(request.POST,instance=cid)
        if updateReq.is_valid():
            updateReq.save()
            request.session.delete()
            return redirect('/')
        else:
            print(updateReq.errors)
            msg="Error!Something went wrong..."
    return render(request,'Profile.html',{'user':user,'cid':cid})

def About(request):
    return render(request,'About.html')

def Contact(request):
    user=request.session.get("user")
    if request.method=="POST":
        newcontact=contactForm(request.POST)
        if newcontact.is_valid():
            newcontact.save()
            print("Your data has been submited!")

             # Email Sending Code
            send_mail(
                subject="Thankyou!",
                message=f"Hello User!\n\nThank you for connecting with us!\nWe will contact you.\n\n\Thanks & Regards!\nShivkali\n+91 9724799469 | shivkali690@gmail.com",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[request.POST['email']],
            )

        else:
            print(newcontact.errors)
    return render(request,'Contact.html',{'user':user})

def userlogout(request):
    logout(request)
    return redirect('/')