from django.shortcuts import render
from django.http import HttpResponse
from .models import productlist
# Create your views here.
"""def product_list(request):
    return render(request,'products.html')"""

def product_list(request):
    data= productlist.objects.all()
    print('Data From Products Table',data)

    content={
        'data': data
    }
    return render(request,'products.html',context=content)