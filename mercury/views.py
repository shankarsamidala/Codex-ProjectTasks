from django.shortcuts import render
from django.http import HttpResponse
from .models import al

# Create your views here.
def cil(request):
    sata=al.objects.all()

    dic={
        'itter':sata
    }
    return render(request,'Aliens2.html',context=dic)