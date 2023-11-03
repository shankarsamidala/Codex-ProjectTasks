from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def productspage(request):
    return HttpResponse('productspage')
