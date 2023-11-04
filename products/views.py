from django.shortcuts import render
from django.http import HttpResponse
from .models import productsList
# Create your views here.
def products_List(request):
    data=productsList.objects.all()
    print('data from product table',data)
    prd={
        'data':data
    }
    return render(request,'products.html',context=prd)
    