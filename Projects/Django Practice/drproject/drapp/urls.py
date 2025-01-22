from django.contrib import admin
from django.urls import path,include
from drapp import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('appointment/',views.appointment),
    path('contact/',views.contact),
    path('feature/',views.feature),
    path('service/',views.service),
    path('team/',views.team),
    path('testimonial/',views.testimonial),
]
