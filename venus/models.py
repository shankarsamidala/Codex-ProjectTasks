from django.db import models

# Create your models here.

class Alien(models.Model):
    Name=models.CharField(max_length=250)
    Spaceship=models.CharField(max_length=250)
    model=models.CharField(max_length=250)
    Price=models.IntegerField(default=100)

    def __str__(self):
        return self.Name