from django.shortcuts import render
from django.http import HttpResponse
from .models import order_list
# Create your views here.


def Orders(request):

    data = order_list.objects.all()

    content = {
        'data':data
    }

    print('data from products table',data)
    return render(request,'orders.html', context=content)