from django.db import models
from datetime import datetime

# Create your models here.
class productsList(models.Model):
    Title=models.CharField(max_length=250)
    Price=models.IntegerField(max_length=250)
    Tag=models.CharField(max_length=250)
    Rating=models.IntegerField(max_length=250)
    create_at=datetime.now()
