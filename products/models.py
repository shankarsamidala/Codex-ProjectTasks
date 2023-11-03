from django.db import models
from datetime import datetime

# Create your models here.
class productsList(models.Model):
    title=models.CharField(max_length=250)
    price=models.IntegerField(default=0)
    tag=models.CharField(max_length=250)
    Rating=models.IntegerField(default=0)
    create_at=datetime.now()