from django.shortcuts import render
from django.http import HttpResponse
from .models import kal
# Create your views here.
def kal(request):
    kali=kal.objects.all()
    lal={
        'ear':kali
    }
    return render(request,'Alian3.html',man=lal)