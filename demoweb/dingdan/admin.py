from django.contrib import admin
from .models import Dingdan

class DingdanAdmin(admin.ModelAdmin):
    list_display = ('buyer','productname','productnumber','productprice','paymoney','paytime','seller')
    search_fields = ('buyer','productname','productnumber','productprice','paymoney','paytime','seller')

admin.site.register(Dingdan, DingdanAdmin)
