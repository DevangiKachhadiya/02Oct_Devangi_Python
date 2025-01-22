from django.contrib import admin
from django.urls import path,include
from doctorapp import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('blog/',views.blog),
    path('blogdetails/',views.blogdetails),
    path('contact/',views.contact),
    path('doctors/',views.doctors),
    path('doctor_list/',views.doctor_list,name='doctor_list'),
    path('doctorprofile/',views.doctorprofile),
    path('login/',views.login),
    path('registration/',views.registration),
    path('showdata/',views.showdata,name='showdata'),
    path('updatedata/<int:id>',views.updatedata),
    path('deletedata/<int:id>',views.deletedata),
]
