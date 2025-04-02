from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import logout
from django.core.mail import send_mail
from MyFinalPro import settings
import random
import string
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    
    user = request.user.email if request.user.is_authenticated else None
    approved = False

    user = request.session.get("user")
    if user :
        try: 
            isapp=Owner.objects.get(email=user)
            approved = isapp.is_approved
        except Owner.DoesNotExist:
            approved= False
    else:
            approved= False
    return render(request, 'index.html', {'user':user, 'approved':approved})

# def login(request):
#     msg = ""
#     user = request.session.get("user")
#     if request.method == 'POST':
#         unm = request.POST["email"]
#         password = request.POST['password']
#         user = UserSignUp.objects.filter(email=unm, password=password)
#         userid = UserSignUp.objects.get(email=unm)
#         print("UserID:", userid.id)
#         if user:
#             print("Login Successfully!")
#             request.session["user"]= unm # session
#             request.session["userid"]=userid.id
#             return redirect("/")
#         else:
#             print("Error! Login Faild...PLZ Try Again...")
#             msg = "Error! Login Faild...PLZ Try Again..."
#     return render(request, 'login.html', {'msg': msg})

def login(request):
    msg = ""
    user = request.session.get("user")

    if request.method == 'POST':
        if 'password' in request.POST:
            unm = request.POST.get("email")
            password = request.POST.get('password')
            try:
                user = UserSignUp.objects.get(email=unm, password=password)
                request.session["user"] = user.email
                request.session["userid"] = user.id
                print("Login Successfully!")
                return redirect("/")
            except UserSignUp.DoesNotExist:
                print("Error! Login Failed. Please Try Again.")
                msg = "Error! Login Failed. Please Try Again."
                         
    return render(request, 'login.html', {'msg': msg,'user':user})



def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('confpass')

        # Validate Email
        user = UserSignUp.objects.filter(email=email).first()
        if not user:
            return render(request, 'reset_password.html')

        # Validate Password Match
        if new_password != confirm_password:
            
            return render(request, 'reset_password.html')

        # Update Password without Hashing
        user.password = new_password
        user.save()

       
        return redirect("/login/")
    return render(request, 'reset_password.html')
       
        
def signUp(request):
    msg = ''
    user = request.session.get("user")
    if request.method == "POST":
        newuser = signupForm(request.POST)
        email = ''

        password = request.POST['password']
        confirm_password = request.POST['confpass']

        if password != confirm_password:
            msg = "Your Password doesn't match Try again..."
            print("Your Password doesn't match Try again...")

        elif newuser.is_valid():
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

    return render(request, 'signUp.html', {'msg': msg, 'newuser':newuser, 'user':user})


def edit_profile(request):
    user = request.session.get("user")
    userid = request.session.get("userid")
    upid = UserSignUp.objects.get(id=userid)
    print("Current User ID:",upid)
    if request.method == "POST":
        updateReq = updateprofileForm(request.POST, instance = upid)
        if updateReq.is_valid():
            updateReq.save()
            request.session.delete()
            return redirect('/login')
        else:
            print(updateReq.errors)
            msg = "Error! Something went wrong...."
    return render(request,'edit_profile.html', {"user": user, "upid":upid})

def add_home(request):
    user = request.session.get("user")
    msg = ""
    errors = []

    if not user:
        return redirect('/login/')  
    
    try:
        owner = Owner.objects.get(email=user)  
    except Owner.DoesNotExist:
        return render(request, "add_home.html", {'msg': 'Owner not found. Please contact support.', 'user': user})

    
    if request.method == 'POST':
        form = addhomeForm(request.POST)
        images = request.FILES.getlist('image')
       
        # Form validation
        if form.is_valid():
           
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
                if not errors:
                # ✅ Create Home and Link Owner
                 home_instance = form.save(commit=False)
                 home_instance.owner = owner
                 home_instance.save()


                # Save images
                for image in images:
                    HomeImage.objects.create(home=home_instance, image=image)
                
                msg = 'Added home successfully with images'
            else:
                msg = 'Error in image upload. Please check the image files.'
        else:
            errors.extend(form.errors.values())
            msg = 'Form has errors. Please check the fields.'
            print(form.errors)

    else:
        form = addhomeForm()

    return render(request, "add_home.html", {'msg': msg, 'errors': errors, 'form': form,'user':user})

def update_home(request,id):
    user = request.session.get('user')
    userid = request.session.get('userid')
    updid = AddHome.objects.get(id=id)
    print("Current User ID:",updid)
    if request.method == 'POST':
        updReq = updatehomeForm(request.POST, instance=updid)
        if updReq.is_valid():
            updReq.save()
            return redirect('/')
        else:
            print(updReq.errors)
            msg = 'Opps! Something went wrong...'
    return render(request, 'update_home.html',{'user':user, 'updid':updid ,'userid':userid})

def buy_home(request):
    user = request.session.get("user")
    query=request.GET.get('query','').strip()
    que=request.GET.get('que','').strip()
    res=AddHome.objects.filter(city_incointains = query) if query else AddHome.objects.none()
    results=AddHome.objects.filter(bedroom_incointains = que) if que else AddHome.objects.none()
    shome = AddHome.objects.filter(htype = 'sell')
    return render(request, 'buy_home.html',{'shome':shome, 'user':user,'query':query, 'que':que, 'res':res, 'results':results})
    

def rent_home(request):
    user = request.session.get('user')
    shome = AddHome.objects.filter(htype = 'rent')
    return render(request, 'rent_home.html',{'shome':shome, 'user':user})

def search_home(request):
    user = request.session.get('user')
    city = request.GET.get('city', '')
    bedroom = request.GET.get('bedroom', '')
    price_range = request.GET.get('price', '')
    search_type = request.GET.get('type', '')

    print(f"city: {city}, Bedroom: {bedroom}, Price: {price_range}, Type: {search_type}")

    filters = {}

    if city:
        filters['city__icontains'] = city
    if bedroom:
        filters['bedroom'] = bedroom
    if search_type == 'buy' and price_range:
        try:
            min_price, max_price = map(lambda x: int(x.replace(',', '').strip()), price_range.split('-'))
            filters['sprice__gte'] = min_price
            filters['sprice__lte'] = max_price
        except ValueError:
            print("Invalid price format for buy")
    elif search_type == 'rent' and price_range:
        try:
            min_price, max_price = map(lambda x: int(x.replace(',', '').strip()), price_range.split('-'))
            filters['rprice__gte'] = min_price
            filters['rprice__lte'] = max_price
        except ValueError:
            print("Invalid price format for rent")

    print(f"Filters Applied: {filters}")

    results = AddHome.objects.filter(**filters)
    return render(request, 'search_home.html', {'results': results, 'user':user})


def cities(request, city):
    user = request.session.get('user')
    homes = AddHome.objects.filter(city__iexact=city)

    return render(request,'cities.html',{'homes':homes, 'city_iexact':city,  'user':user})

  

def about_us(request):
    user = request.session.get("user")
    return render(request, 'about_us.html', {'user':user})

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



def show_home(request):
    user = request.session.get('user')
    home = AddHome.objects.prefetch_related('images').all()
    return render(request, 'show_home.html',{'home':home, 'user':user})

def apply_owner(request):
    msg=''
    user = request.session.get('user')
    if request.method == 'POST':
        own=apply_ownerForm(request.POST)
        if own.is_valid():
            ownerr=own.save()
            ownerr.user = request.user
            ownerr.approval_status = 'Pending'
            ownerr.save()
            msg="Applied successfully!"
            print('Applied successfully!')
            redirect('/')
        else:
            print(own.errors)
            msg='Error! Something went wrong...'
            print('Error! Something went wrong...')
    return render(request, 'apply_owner.html', {'msg':msg, 'user':user})



def userlogout(request):
    logout(request)
    return redirect('/')

def show_buy_home(request,id):
    user = request.session.get('user')
    sbh=AddHome.objects.get(id=id)
    images = HomeImage.objects.filter(home=sbh)[:5]  # Get first 5 images
    remaining_images_count = HomeImage.objects.filter(home=sbh) 
    selected_home = request.GET.get('home', '1')  
    print("id",id)
  

    
    return render(request, 'show_buy_home.html',{ 'user':user, 'sbh':sbh, 'images':images, 'remaining_images_count':remaining_images_count , '':selected_home})



def show_rent_home(request,id):
    sbh=AddHome.objects.get(id=id)
    images = HomeImage.objects.filter(home=sbh)[:5]  # Get first 5 images
    remaining_images_count = HomeImage.objects.filter(home=sbh) 
    selected_home = request.GET.get('home', '1')  
    print("id",id)
  

    
    return render(request, 'show_rent_home.html',{'sbh':sbh, 'images':images, 'remaining_images_count':remaining_images_count , '':selected_home})

def your_properties(request):
    user = request.session.get('user')
    
    if not user:
        print("User not logged in. Redirecting to login page.")
        return render(request, 'your_properties.html', {'error': 'Please log in to view your properties.'})

    try:
        owner = Owner.objects.get(email=user)
        print(f"Owner Found: {owner}")

        # Check if properties are linked
        properties = AddHome.objects.filter(owner=owner)
        if properties.exists():
            print(f"Properties Linked: {properties}")
            for prop in properties:
             print(f"Name: {prop.hname}, Address: {prop.address}, Type: {prop.htype}")
        else:
            print("No properties linked to this owner.")
            return render(request, 'your_properties.html', {'error': 'No properties found.'})

    except Owner.DoesNotExist:
        print("Owner does not exist. Please register.")
        return render(request, 'your_properties.html', {'error': 'Owner not found. Please register.'})

    return render(request, 'your_properties.html', {'properties': properties, 'user': user})


def delete_home(request, id):
   dh=AddHome.objects.get(id=id)
   AddHome.delete(dh)
   return redirect('your_properties')

def show_your_properties(request,id):
    user = request.session.get('user')
    sbh=AddHome.objects.get(id=id)
    images = HomeImage.objects.filter(home=sbh)[:5]  # Get first 5 images
    remaining_images_count = HomeImage.objects.filter(home=sbh) 
    selected_home = request.GET.get('home', '1')  
    print("id",id)
  
    return render(request, 'show_your_properties.html',{'sbh':sbh, 'images':images, 'remaining_images_count':remaining_images_count , '':selected_home, 'user':user}
)

def rs_search(request):
    user = request.session.get('user')
    query=request.GET.get('query','').strip()
    res=AddHome.objects.filter(city__icontains = query) if query else AddHome.objects.none()

    
    return render(request, 'rs_search.html',{'query':query, 'user':user, 'res':res})