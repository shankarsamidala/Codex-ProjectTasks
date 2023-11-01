from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def productpage(request):
    return render(request,'products.html')
