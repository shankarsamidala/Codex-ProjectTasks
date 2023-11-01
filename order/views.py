

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def OrderPage(request):
    return HttpResponse('Welcome to orderpage')