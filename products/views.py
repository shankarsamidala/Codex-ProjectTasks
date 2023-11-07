from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductList

# Create your views here.

def productlist(request):
   
    data1 = ProductList.objects.all()
     
    content = {
        'data':data1
     }
    
    return render(request,'product.html',context=content) 