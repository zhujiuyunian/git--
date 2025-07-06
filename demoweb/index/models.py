from django.db import models

# Create your models here.
class Index(models.Model):
    name= models.CharField(max_length=255)
    url=models.URLField(max_length=2000)
    img_url=models.URLField(max_length=2000,default="https://ts3.tc.mm.bing.net/th/id/OIP-C.ThRuhUBIyjg4RPQLDYBN2AHaHa?rs=1&pid=ImgDetMain&o=7&rm=3",blank=True)