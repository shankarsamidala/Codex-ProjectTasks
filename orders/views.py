#from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

#def OrderList(request):
#    return HttpResponse('Orders List')
from django.shortcuts import render
from django.http import HttpResponse
from .models import OrderList
# Create your views here.

def Orders(request):
    data=OrderList.objects.all()
    
    #print('Data from Products table',data)
    
    #for i in data:
    #    if i.price >= 25000:
    #       print(i.price)
    
    orders = {
       'data' : data
    }
    print('data from products table',data)
    return render(request,'orders.html',context=orders)