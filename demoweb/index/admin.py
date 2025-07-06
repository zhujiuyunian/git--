from django.contrib import admin
from .models import Index

class IndexAdmin(admin.ModelAdmin):
    list_display=("name","url","img_url")
    search_fields =("name","url","img_url")
# Register your models here.
admin.site.register(Index, IndexAdmin)
