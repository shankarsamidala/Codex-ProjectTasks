from django.db import models

# Create your models here.

class ProductList(models.Model):
    Title = models.CharField(max_length=200)
    Price = models.IntegerField(default=0)
    Tag = models.CharField(max_length=200)
    Rating = models.CharField(max_length=200)
    model = models.CharField(max_length=200,default=0)