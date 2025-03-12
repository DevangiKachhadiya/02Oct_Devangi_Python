from django.contrib import admin
from django.urls import path
from myapp import views 

urlpatterns = [
    path('', views.index, name='/'),
    path('login/',views.login, name='login'),
    path('signUp/', views.signUp, name='signUp'),
]
