from django.db import models
from datetime import datetime
# Create your models here.


class ProductsList(models.Model):
    name = models.CharField(max_length=250)
    tag = models.CharField(max_length=250)
    price = models.IntegerField()
    rating = models.IntegerField(default=0)
    created_at = datetime.now()

    
