from django.contrib import admin
from .models import *

# Register your models here.

class empdata(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','name','emp_id','email','password']

admin.site.register(Employee,empdata)