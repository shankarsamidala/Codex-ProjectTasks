from django.db import models
from products.models import ProductsList
# Create your models here.
class OrderList(models.Model):
    Product=models.OneToOneField(ProductsList,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Product.title
