from django.contrib import admin
from django.urls import path
from myapp import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='/'),
    path('log_in/',views.login, name='log_in'),
    path('signUp/', views.signUp, name='signUp'),
    path('add_homee/', views.add_homee, name='add_homee'),
    path('buy_home/', views.buy_home, name='buy_home'),
    path('rent_home/', views.rent_home, name='rent_home'),
    path('extra/', views.extra, name='extra'),
    path('latest_extra/', views.latest_extra, name='latest_extra'),
    path('searchbar/', views.searchbar, name='searchbar'),
    path('show_home/', views.show_home, name='show_home'),
    path('slider_section/',views.slider_section, name='slider_section')
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
