from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Society)
admin.site.register(House)
admin.site.register(Complaint)
admin.site.register(HouseListing)
admin.site.register(Message)


class HouseAdmin(admin.ModelAdmin):
    list_display = ('house_number', 'society', 'owner')
    search_fields = ('house_number', 'owner__username', 'society__name')


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('member', 'house', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('member__username', 'house__house_number')