from django.db import models

# Create your models here.

class mobiles(models.Model):
    title = models.CharField(max_length=220)
    price = models.CharField(max_length=220)
    tag = models.CharField(max_length=220)
