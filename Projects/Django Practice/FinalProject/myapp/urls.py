from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.index),
    path('signup/',views.signup,name='signup'),
    path('Notes/',views.Notes,name='Notes'),
    path('Profile/',views.Profile,name='Profile'),
    path('About/',views.About,name='About'),
    path('Contact/',views.Contact,name='Contact'),
    path('userlogout/',views.userlogout),
]
