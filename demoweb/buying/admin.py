from django.contrib import admin
from .models import Products
class Productsadmin(admin.ModelAdmin):
    list_display=("name",'number','price')
    search_fields=("name",'description','img_url','number','price')

# Register your models here.
admin.site.register(Products,Productsadmin)