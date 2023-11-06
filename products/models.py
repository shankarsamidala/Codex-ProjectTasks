from django.db import models

# Create your models here.
class productList(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField(default=0)
    tag = models.CharField(max_length=250)
    rating = models.CharField(max_length=250)
    modelname=models.CharField(max_length=250)

