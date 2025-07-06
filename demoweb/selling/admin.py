from django.contrib import admin
from .models import Sellproduct

class Sellproductadmin(admin.ModelAdmin):
    list_display=("name","price",'img_url','description','number')
    search_fields=("name","price",'img_url','description','number')

admin.site.register(Sellproduct,Sellproductadmin)
