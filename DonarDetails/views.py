from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Donars(request):
    return HttpResponse('The donars available are:')