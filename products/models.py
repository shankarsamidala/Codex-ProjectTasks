from django.db import models
from datetime import datetime
class productslist(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    rating = models.IntegerField()
    create_at= datetime.now()


