from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
import random, string
from .models import Owner
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Home
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import HomeForm

# Create your views here.

def create_owner(email, username):
    temp_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))  # Generate password
    owner = Owner.objects.create(
        email=email,
        username=username,
        password=make_password(temp_password),  # Hash the password
        is_first_login=True
    )

    # Send email with credentials
    send_mail(
        'Your E-Housing Account',
        f'Hello {username},\nYour temporary password is: {temp_password}\nPlease log in and change it immediately.',
        'admin@ehousing.com',
        [email],
        fail_silently=False,
    )

    return owner

@login_required
def dashboard(request):
    if request.user.is_first_login:
        return redirect('change_password')  # Redirect to change password
    return render(request, 'dashboard.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            user.is_first_login = False  # Mark that they changed their password
            user.save()
            update_session_auth_hash(request, user)  # Prevent logout after password change
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


@login_required
def owner_home_list(request):
    homes = Home.objects.filter(owner=request.user)  # Only show the logged-in owner's homes
    return render(request, 'owner/home_list.html', {'homes': homes})


@login_required
def add_home(request):
    if request.method == "POST":
        form = HomeForm(request.POST)
        if form.is_valid():
            home = form.save(commit=False)
            home.owner = request.user  # Assign the logged-in owner
            home.save()
            return redirect('owner_home_list')  # Redirect to home list
    else:
        form = HomeForm()
    return render(request, 'owner/add_home.html', {'form': form})