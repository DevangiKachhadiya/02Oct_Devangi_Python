from django.contrib import admin
from .models import *
# Register your models here.


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'address')
    search_fields = ('username', 'email')
admin.site.register(Owner)

class HouseAdmin(admin.ModelAdmin):
    list_display = ('owner', 'address', 'price', 'status')
    list_filter = ('status',)
    search_fields = ('address', 'owner__username')
admin.site.register(House)


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('member', 'issue', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('member__username', 'issue')
admin.site.register(Complaint)
