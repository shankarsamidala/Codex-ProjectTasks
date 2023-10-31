from django.db import models

# Create your models here.
class ProductInfo(models.Model):
    name=models.CharField(max_length=299)
    price=models.IntegerField(default=1000)
    offer=models.IntegerField()
    tag=models.CharField(max_length=50)
    rating=models.CharField(max_length=25)