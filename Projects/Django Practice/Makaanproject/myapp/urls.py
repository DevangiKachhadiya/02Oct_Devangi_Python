from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('property-agent/',views.property_agent),
    path('property-list/',views.property_list),
    path('property-type/',views.property_type),
    path('testimonial/',views.testimonial),
]
