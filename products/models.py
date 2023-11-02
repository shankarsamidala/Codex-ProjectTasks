from django.db import models

# Create your models here.

class Productlist(models.Model):
    tittle=models.CharField(max_length=250)
    price=models.IntegerField(default=0)
    tag=models.CharField(max_length=250)
    rating=models.IntegerField()