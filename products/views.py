from django.shortcuts import render
from django.http import HttpResponse
from .models import productList

# Create your views here.

def products(request):

    data = productList.objects.all()

    print(data)

    Products = {
        'data' :data
    }

    return render(request,'products.html', context=Products)
