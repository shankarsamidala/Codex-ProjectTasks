from django.db import models
from datetime import datetime

# Create your models here.
class productsList(models.Model):
    title=models.CharField(max_length=250)
    price=models.IntegerField(default=250)
    Tag=models.CharField(max_length=250)
    Rating=models.IntegerField(default=250)
    create_at=datetime.now()