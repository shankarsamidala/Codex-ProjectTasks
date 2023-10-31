from django.shortcuts import render
from django.http import HttpResponse
#eate your views here.
def home(request):
    return HttpResponse('hello')