from django.db import models
from datetime import datetime

# Create your models here.
class productsList(models.Model):
     title=models.CharField(max_length=250)
     price=models.IntegerField(max_length=250)
     tag=models.CharField(max_length=250)
     rating=models.IntegerField(max_length=250)
     create_at=models.DateTimeField(default=datetime.now())


     def __str__ (self):
         return self.name 