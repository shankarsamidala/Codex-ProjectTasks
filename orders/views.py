from django.shortcuts import render
from django.http import HttpResponse
from .models import orderslist
# Create your views here.
def Orders(request):
    data=orderslist.objects.all()
    content={
        'data':data
    }
    print('Data From Products Table',data)
    return render(request,'orders.html',context=content)
    