from django.contrib import admin
from django.urls import path
from adminapp import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
   path('adminlogin/',views.adminlogin, name='adminlogin'),
   path('dashboard/',views.dashboard, name='dashboard'),
   path('addCategory/',views.addCategory, name='addCategory'),
   path('addProduct/',views.addProduct, name='addProduct'),
   path('viewProducts/',views.viewProducts, name='viewProducts'),
   path('editProduct/<int:id>/', views.editProduct, name='editProduct'),
   path('deleteProduct/<int:id>/', views.deleteProduct, name='deleteProduct'),
   path('viewCategories/',views.viewCategories, name='viewCategories'),
   path('requestedProducts/',views.requestedProducts, name='requestedProducts'),
   path('approveProduct/<int:id>', views.approveProduct, name='approveProduct'),
   path('rejectProduct/<int:id>', views.rejectProduct, name='rejectProduct'),
   path('userlogout/',views.userlogout),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)