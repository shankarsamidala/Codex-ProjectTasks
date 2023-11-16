from django.db import models

# Create your models here.
class donarsdetails(models.Model):
    name=models.CharField(max_length=250)
    age=models.IntegerField(default=0)
    Blood_group=models.CharField(max_length=250)
    location=models.CharField(max_length=250)
    phoneno=models.IntegerField(default=0)