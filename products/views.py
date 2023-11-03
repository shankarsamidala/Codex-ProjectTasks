from django.shortcuts import render
from django.http import HttpResponse
from .models import productList
# Create your views here
def productlist(request):
 data=productList.objects.all()
 content={
 'data':data
 }
 
 return render(request,'products.html',context=content)
