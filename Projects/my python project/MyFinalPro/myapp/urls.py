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
    path('search_home/', views.search_home, name='search_home'),
    path('cities/<str:city>', views.cities, name='cities'),
    path('apply_owner/', views.apply_owner, name='aplly_owner'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('update_home/<int:id>',views.update_home, name='update_home'),
    path('userlogout/',views.userlogout),
    path('show_buy_home/<int:id>',views.show_buy_home, name='show_buy_home'),
    path('show_rent_home/<int:id>',views.show_rent_home, name='show_rent_home'),
    path('your_properties/',views.your_properties, name='your_properties'),
    path('delete_home/<int:id>',views.delete_home, name='delete_home'),
    path('show_your_properties/<int:id>', views.show_your_properties),
    path('rs_search/',views.rs_search),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
