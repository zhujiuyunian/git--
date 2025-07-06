from django.db import models

# Create your models here.
class Useraccount(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    money=models.FloatField(default=100.00)
    appname=models.CharField(max_length=100,default='',blank=True,null=True)
