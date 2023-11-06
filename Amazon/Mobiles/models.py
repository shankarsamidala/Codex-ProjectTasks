from django.db import models

# Create your models here.
class moi(models.Model):
    model=models.CharField(max_length=250)
    ROM=models.IntegerField()
    RAM=models.IntegerField()
    Processor=models.CharField(max_length=250)
    def __str__(self):
        return self.model