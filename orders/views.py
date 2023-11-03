from django.shortcuts import render
from django.http import HttpResponse
from .models import orders_list

# Create your views here.
def Order(request):
    data = orders_list.objects.all()
    content = {
        'data':data

    }
    print('data from products table',data)
    return render(request,'orders.html',context=content)
