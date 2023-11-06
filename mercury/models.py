from django.db import models
from datetime import datetime
from venus.models import Alien

# Create your models here.
class al(models.Model):
    ali=models.OneToOneField(Alien,on_delete=models.CASCADE,default=1)


    def __str__(self):
        return self.ali.Name