from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductList

# Create your views here.

def ProductsList(request):

    data = ProductList.objects.all()
    print('data from products table',data)

    content={
        'data':data
    }
    return render(request,'products.html',context=content)
