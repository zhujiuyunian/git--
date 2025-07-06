from django.db import models

# Create your models here.
class Products(models.Model):
    username=models.CharField(max_length=100,default='user')
    buyname=models.CharField(max_length=100,default='null',null=True,blank=True)
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    img_url=models.URLField(max_length=1000,default='',null=True,blank=True)
    number=models.FloatField(default=1000.0,null=True,blank=True)
    price=models.FloatField(default=10.00,null=True,blank=True)
