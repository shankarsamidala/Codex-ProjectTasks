from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Order(request):
    return HttpResponse('HERE, We can placed your orders')