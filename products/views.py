from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductsList
# Create your views here.

def ProductList(request):
    data=ProductsList.objects.all()
    
    #print('Data from Products table',data)
    
    #for i in data:
    #    if i.price >= 25000:
    #       print(i.price)
    
    products = {
       'data' : data
    }
    
    return render(request,'products.html',context=products)