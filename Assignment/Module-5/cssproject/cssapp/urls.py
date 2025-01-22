from django.contrib import admin
from django.urls import path,include
from cssapp import views

urlpatterns = [
    path('',views.index),
    path('basic/',views.basic),
    path('doctor/',views.doctor),
]
