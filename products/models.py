from django.db import models

# Create your models here.
class productslist(models.Model):
    title=models.CharField(max_length=250)
    price=models.IntegerField(default=0)
    tag=models.CharField(max_length=250)
    rating=models.CharField(max_length=250)
    model=models.CharField(max_length=250,default=0)