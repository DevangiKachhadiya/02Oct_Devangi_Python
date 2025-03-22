from django.contrib import admin
from django.urls import path,include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='/'),
    path('login/', views.login, name='login'),
    path('signUp/', views.signUp, name='signUp'),
    path('add_home/', views.add_home, name='add_home'),
    path('show_home/', views.show_home, name='show_home'),
    path('rent_home/', views.rent_home, name='rent_home'),
    path('buy_home/', views.buy_home, name='buy_home'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('page404/', views.page404, name='page404'),
    path('page500/', views.page500, name='page500'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('search_home/', views.search_home, name='search_home'),
    path('cities/<str:city>', views.cities, name='cities'),
    path('apply_owner/', views.apply_owner, name='aplly_owner'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)