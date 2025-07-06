from django.contrib import admin
from .models import Useraccount

class Useraccountadmin(admin.ModelAdmin):
    list_display=('username','password')
    search_fields=('username','password')
# Register your models here.
admin.site.register(Useraccount,Useraccountadmin)