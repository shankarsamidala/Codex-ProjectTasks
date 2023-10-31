from django.shortcuts import render
from django.shortcuts import HttpResponse

def Home(request):
    return HttpResponse('Welcome Back!')
