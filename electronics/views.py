from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ElectronicList(request):
    return HttpResponse('Electronics List')