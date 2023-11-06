from django.db import models


# Create your models here.
class kal(models.Model):
    oceans=models.CharField(max_length=250)
    lenght=models.IntegerField()
    depth=models.IntegerField()

    def __str__(self):
        return self.oceans
