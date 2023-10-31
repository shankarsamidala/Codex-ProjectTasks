from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ProductPage(request):
    return HttpResponse('Product page Response')