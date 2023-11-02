from django.shortcuts import render
from django.http import HttpResponse
from .models import orders_list

# Create your views here.

def ordersList(request):
 data=orders_list.objects.all()
 print('data from products table',data)
 prd={
    'data':data
 }
 return render(request,'orders.html',context=prd)