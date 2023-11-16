from django.shortcuts import render
from django.http import HttpResponse
from .models import carrot 
# Create your views here.
def home(request):
    data=carrot.objects.all()
    veg={
        'accounts':data
    }
    return render(request,'gms.html',context=veg)