from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   path('index/',views.index),
   path('signup/',views.signup),
   path('login/',views.login),
   path('',views.base),
   path('Appointment/',views.Appointment),
   path('doctor/',views.doctor),
   path('patient/',views.patient),
   path('contact/',views.contact),

]
