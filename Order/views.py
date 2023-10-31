from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def OrderPage(request):
    return HttpResponse('This is order page')
