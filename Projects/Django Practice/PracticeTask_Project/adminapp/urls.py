from django.contrib import admin
from django.urls import path
from adminapp import views

urlpatterns = [
   path('adminlogin/',views.adminlogin, name='adminlogin'),
   
]
