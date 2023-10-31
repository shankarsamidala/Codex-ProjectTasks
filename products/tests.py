from django.test import render
from django.Http import HttpResponce

# Create your tests here.


def productList(request):
    return HttpResponce('products page')