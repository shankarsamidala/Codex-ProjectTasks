from django.test import TestCase
from django.Http import HttpResponce

# Create your tests here.


def productlist(request):
    return HttpResponce('products page')
