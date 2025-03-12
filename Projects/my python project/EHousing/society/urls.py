from django.contrib import admin
from django.urls import path  
from society import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
   path('',views.index),
   path('about/',views.about), 
   path('contact/',views.contact),
   path('gallery/',views.gallery, name='gallery'),
   path('properties/',views.properties),
   path('service/',views.service),
   path('login/',views.login),
   path('signup/',views.signup),
   path('userlogout/',views.userlogout),
   path('updprofile/',views.updprofile, name='updprofile'),
   path('addhouse/',views.addhouse, name = 'addhouse'),
   path('complaints/',views.complaints, name='complaints'),
   path('showhome/',views.showhome, name='showhome'),
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
