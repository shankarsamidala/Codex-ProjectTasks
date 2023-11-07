from django.db import models

# Create your models here.

class ProductList(models.Model):
    title=models.CharField(max_length=250)
    model=models.IntegerField()
    rating=models.IntegerField()
    price=models.IntegerField()
    tag=models.CharField(max_length=250)

def __str__ (self):
    return self.title
