from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductList
# Create your views here.



def Product_List(request):
    data= ProductList.objects.all()
    print('Data From Products Table',data)

    content={
        'data': data
    }
    return render(request,'products.html',context=content)
