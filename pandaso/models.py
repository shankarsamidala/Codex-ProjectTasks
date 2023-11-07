from django.db import models
from pandasp.models import products

# Create your models here.
class orders(models.Model):
    pandasp= models.OneToOneField(products,on_delete=models.CASCADE)
    def __str__(self):
     return self.pandasp.name