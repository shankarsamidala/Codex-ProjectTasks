from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductsList
# Create your views here.

def ProductList(request):
    data=ProductsList.objects.all()
    products = {
        'data':data
    }
    return render(request,'products.html',context=products)