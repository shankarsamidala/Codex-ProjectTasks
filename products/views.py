from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def Products(request):
    return HttpResponse('Product Page')
