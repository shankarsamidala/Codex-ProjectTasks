from django.shortcuts import render
from django.http import HttpResponse
from .models import productlist

# Create your views here.

def productslist(request):
 data=productlist.objects.all()
 print('data frim products table',data)
 prd={
    'data':data
 }
 return render(request,'products.html',context=prd)