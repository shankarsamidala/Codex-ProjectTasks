from django.db import models
from products.models import productsList

# Create your models here.
class orderslist(models.Model):
    product=models.OneToOneField(productsList,on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return self.product.title
