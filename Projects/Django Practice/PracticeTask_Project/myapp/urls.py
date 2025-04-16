from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
   path('',views.index, name='index'),
   path('home/',views.home, name='home'),
   path('login/',views.login, name='login'),
   path('signUp/',views.signUp, name='signUp'),
   path('reqProduct/',views.reqProduct, name='reqProduct'),
   path('vpro/', views.vpro, name='vpro'),
] 