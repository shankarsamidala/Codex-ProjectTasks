from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Orders(request):
    return HttpResponse('OrdersPage')