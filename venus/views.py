from django.shortcuts import render
from django.http import HttpResponse
from .models import Alien

# Create your views here.
def sat(request):
    return HttpResponse("This is venus")
def gat(request):
    sata=Alien.objects.all()

    dic={
        'itter':sata
    }
    return render(request,'Aliens.html',context=dic)