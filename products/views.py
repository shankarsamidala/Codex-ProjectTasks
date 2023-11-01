from django.shortcuts import render
from .models import productsList

# Create your views here.
def ProductPage(request):
    return(request,'products.html')