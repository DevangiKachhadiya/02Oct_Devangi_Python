from django.contrib import admin
from .models import *

# Register your models here.

class owneradmin(admin.ModelAdmin):
    list_display= ('name', 'email','number', 'is_approved') 
    list_filter = ('is_approved',)
    actions = ['approved_owners', 'rejected_owners']

    def approved_owners(self, request, queryset):
        queryset.update(STATUS_CHOICE= 'Approved')
    approved_owners.short_description = "Approve selected owners"

    def rejected_owners(self, request, queryset):
        queryset.update(STATUS_CHOICE= 'Rejected')
    approved_owners.short_description = "Reject selected owners"



admin.site.register(Owner,owneradmin)