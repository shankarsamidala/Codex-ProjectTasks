from django.shortcuts import render
from django.http import HttpResponse

def ProductPage(request):
    return HttpResponse('Welcome to ProductPage')

def HomePage(request):
    return HttpResponse('Welcome to HomePage')