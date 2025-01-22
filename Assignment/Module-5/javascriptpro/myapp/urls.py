from django.db import models
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.urls import path
from . import views

urlpatterns = [
    path('contact/',views.contact_view, name='contact'),
    path('register/', views.register_patient, name='register'),
    path('validate_email/', views.validate_email, name='validate_email'),
    path('success/', lambda request: render(request, 'success.html'), name='success'),
]

