from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ProductsList(request):
    return HttpResponse('product page')