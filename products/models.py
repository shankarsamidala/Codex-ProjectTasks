from django.db import models
from datetime  import datetime

# Create your models here.
class ProductList(models.Model):
    title = models.CharField(max_length=250)
    tag = models.CharField(max_length=250)
    price = models.IntegerField()
    rating = models.IntegerField()
    created_at = datetime.now()