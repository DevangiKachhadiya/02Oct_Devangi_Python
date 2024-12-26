from django.contrib import admin
from django.urls import path,include
from Christmasapp import views

urlpatterns = [
    path('',views.index),
    path('login/',views.login),
]
