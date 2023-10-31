from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Electronics(request):
    return HttpResponse('electronic equipments')