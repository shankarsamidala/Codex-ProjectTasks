from django.db import models

# Create your models here.
class ProductList(models.Model):
    title=models.CharField(max_length=250)
    price=models.IntegerField()
    tag=models.CharField(max_length=50)
    rating=models.IntegerField()