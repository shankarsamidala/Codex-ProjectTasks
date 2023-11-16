from django.db import models
from django.db import models

# Create your models here.
class doctorinfoList(models.Model):
    doctorName=models.CharField(max_length=250)
    specialization=models.CharField(max_length=250)
    phone=models.IntegerField(default=0)
    cost=models.IntegerField(default=0)
