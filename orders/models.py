from django.db import models
from products.models import ProductList
# Create your models here.
class orders_list(models.Model):
    product= models.OneToOneField(ProductList,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.product.tag