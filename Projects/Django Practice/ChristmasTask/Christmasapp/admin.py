from django.contrib import admin
from .models import *

# Register your models here.

class santaData(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','email','password','address','city']

admin.site.register(Santa,santaData)

class loginData(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','first_name','last_name','email','password']

admin.site.register(Login,loginData)