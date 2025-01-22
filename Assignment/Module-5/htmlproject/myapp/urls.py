from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.html1),
    path('jango/',views.jango),
    path('doctor/',views.doctor),
]
