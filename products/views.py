from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductList
# Create your views here.



def ProductList(request):
    return render(request,'products.html')
