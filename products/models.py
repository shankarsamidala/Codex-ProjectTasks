from django.db import models
from datetime import datetime
# Create your models here.
class productlist(models.Model):
    title=models.CharField(max_length=250)
    price=models.IntegerField()
    rating=models.IntegerField()
    tag=models.CharField(max_length=250)
    created_at=datetime.now()
    