from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductsList

# Create your views here.
def myapp(request):
    a=ProductsList.objects.all()
    product={
        'data':a
    }
    return render(request,'index.html',context=product)