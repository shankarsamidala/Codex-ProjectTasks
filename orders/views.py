from django.shortcuts import render
from django.http import HttpResponse
from .models import orders_list


# Create your views here.

def orders(request):
    data=orders_list.objects.all()
    print('Data from Products Table',data)

    prd={
        'data':data
    }
    return render(request,'orders.html',context=prd)