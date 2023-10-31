from django.db import models


# Create your models here.
class productlist(models.Model):
    Title=models.CharField(max_length=250)
    Place=models.CharField(max_length=250)
    Price=models.IntegerField()
    Ratings=models.IntegerField(default=0)

