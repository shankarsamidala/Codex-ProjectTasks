from django.shortcuts import render
from django.http import HttpResponse
from .models import OrderList
# Create your views here.

def Orders(request):
    data=OrderList.objects.all()
    orders = {
        'data':data
    }
    print('data from products table',data)
    return render(request,'orders.html',context=orders)