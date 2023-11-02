from django.shortcuts import render
from django.http import HttpResponse
from .models import productlist
# Create your views here.
def productList(request):
     data=productlist.objects.all()

     content={
        'data':data
     }

     return render(request,'products.html',context=content)