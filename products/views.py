from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def productlist(request):
    return HttpResponse('PRODUCTS PAGE')