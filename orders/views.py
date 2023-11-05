from django.shortcuts import render
from django.http import HttpResponse
from .models import orderlist
# Create your views here.

def order_list(request):
    data= orderlist.objects.all()
    print('Data From Products Table',data)

    content={
        'data': data
    }
    return render(request,'orders.html',context=content)