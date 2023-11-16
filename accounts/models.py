from django.db import models

# Create your models here.
class carrot(models.Model):
    accountholdername=models.CharField(max_length=500)
    branchaname=models.CharField(max_length=250)
    accountnumber=models.IntegerField(default=0)

def __str__(self):
    return self.accountholdername
