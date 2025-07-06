from django.db import models
from datetime import datetime

# Create your models here.
class Dingdan(models.Model):
    buyer = models.CharField(max_length=100,default='buyer')
    productname = models.CharField(max_length=100,default='productname')
    productnumber = models.IntegerField(default=0)
    productprice = models.FloatField(default=0.0)
    paymoney = models.FloatField(default=0.0)
    paytime = models.CharField(default=str(datetime.now()))
    seller = models.CharField(max_length=100,default='seller')
