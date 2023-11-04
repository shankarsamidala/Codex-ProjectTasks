from django.db import models
from datetime import datetime

# Create your models here.
class productslist(models.Model):
 title=models.CharField(max_length=250)
 price=models.IntegerField(default=0)
 rating=models.IntegerField(default=0)
 tag=models.CharField(max_length=250)
 create_at=models.DateTimeField(default=datetime.now())

def _str_(self):
    return self.name
 