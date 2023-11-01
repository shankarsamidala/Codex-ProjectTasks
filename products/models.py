from django.db import models
from datetime import datetime

# Create your models here.
class productsList(models.Model):
    title=models.CharField(max_length=250)
    Price=models.IntegerField(max_length=250)
    Tag=models.CharField(max_length=250)
    Rating=models.IntegerField(max_length=250)
    create_at=models.DateTimeField(default=datetime.now)
    def _str_(self):
        return self.name