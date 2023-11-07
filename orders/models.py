from django.db import models
from products.models import ProductList

# Create your models here.
class Order_List(models.Model):
    Product=models.OneToOneField(ProductList,on_delete=models.CASCADE)


    def __str__(self):
        return self.Product.title
