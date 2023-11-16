from django.db import models


# Create your models here.
class ComplaintsList(models.Model):
    ComplainantName =models.CharField(max_length=250)
    ComplainantID=models.IntegerField(default=0)
    ComplaintNumber=models.IntegerField(default=0)
    RegDate=models.DateTimeField(auto_now_add=True)
    State=models.CharField(max_length=250)
    Category=models.CharField(max_length=250)
    SubCategory=models.CharField(max_length=250)
    ComplaintDetails=models.TextField()
    
