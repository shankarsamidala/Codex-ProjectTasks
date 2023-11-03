from django.db import models
from datetime import datetime
class productsList(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    rating = models.IntegerField()
    create_at= datetime.now()
    milage = models.IntegerField(default=50)
    def __str__(self):
        return self.title

