from django.db import models
from datetime import datetime

# Create your models here.
class ProductList(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    tag = models.CharField(max_length=250)
    rating = models.IntegerField()
    created_at = datetime.now()

    