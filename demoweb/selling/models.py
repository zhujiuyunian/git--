from django.db import models

# Create your models here.
class Sellproduct(models.Model):
    username = models.CharField(max_length=100,default='user')
    appname = models.CharField(max_length=100,default='user')
    name = models.CharField(max_length=100,default='null',null=True,blank=True)
    price =models.FloatField(default=0.0)
    img_url=models.URLField(max_length=2000,default='null',null=True,blank=True)
    description=models.CharField(max_length=200,default='null',null=True,blank=True)
    number = models.FloatField(default=0.0)