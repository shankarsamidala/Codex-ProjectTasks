from django.db import models
from datetime import datetime
# Create your models here.
class productList(models.Model): 
    name = models.CharField(max_length=250)
    tag = models.CharField(max_length=250)
    price = models.IntegerField()
    rating= models.IntegerField() 
    model=models.IntegerField(default=0)

    def __str__(self):
        return self.name


