from django.db import models
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.shortcuts import render
from .forms import *


# Create your views here.
def contact_view(request):
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def register_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PatientForm()
    return render(request, 'register.html', {'form': form})

@csrf_exempt
def validate_email(request):
    data = json.loads(request.body)
    email = data.get("email")
    if Patient.objects.filter(email=email).exists():
        return JsonResponse({"valid": False, "message": "Email already exists."})
    return JsonResponse({"valid": True})
