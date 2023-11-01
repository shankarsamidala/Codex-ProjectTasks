from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def mat(request):
    return HttpResponse('This is mercury')