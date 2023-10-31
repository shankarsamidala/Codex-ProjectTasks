from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ProductPage(request):
    return HttpResponse('Welcom to Product Page')
def HomePage(request):
    return HttpResponse('Welcome to home Page')
