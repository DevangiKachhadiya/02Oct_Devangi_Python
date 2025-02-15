from django.contrib import admin
from django.urls import path,include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('',views.index),
   path('signup/',views.signup),
   path('profile/',views.profile, name='profile'),
   path('login/',views.login),
   path('userlogout/',views.userlogout),
   path('base/',views.base),
   path('Appointment/',views.Appointment),
   path('showapp/',views.showapp, name='showapp'),
   path('deleteapp/<int:id>',views.deleteapp, name='deleteapp'),
   path('doctor/',views.doctor),
   path('patient/',views.patient, name='patient'),
   path('about/',views.about),
   path('contact/',views.contact),
   # path('dashboard/',views.admindash),
   path('adddoctor/',views.adddoctor, name='adddoctor'),
   path('showdoctors/',views.showdoctors,name='showdoctors'),
   # path('otpverify/',views.otpverify, name='otpverify'),
   path('forgotpass/',views.forgotpass, name='forgotpass'),
   path('adminn/',views.adminn),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)