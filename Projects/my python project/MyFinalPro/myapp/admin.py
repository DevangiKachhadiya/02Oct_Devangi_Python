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


class AddHomeAdmin(admin.ModelAdmin):
    list_display = ('hname','address','city','size','bedroom','desc','htype','sprice','rprice')


admin.site.register(AddHome, AddHomeAdmin)


class HomeImageAdmin(admin.ModelAdmin):
    list_display = ('home','image')

admin.site.register(HomeImage,HomeImageAdmin)


class UserSignUpAdmin(admin.ModelAdmin):
    list_display = ('fnm','lnm','email','password','confpass')

admin.site.register(UserSignUp,UserSignUpAdmin)



class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','phoneno','imessage')


admin.site.register(Contact, ContactAdmin)


class reqtourAdmin(admin.ModelAdmin):
    list_display = ('date','name','rtuemail','contact')


admin.site.register(reqtour)