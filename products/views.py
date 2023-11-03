from django.shortcuts import render
from .models import productsList
# Create your views here.
def productslist(request):
        data=productsList.objects.all()
        print('data from products table', data)
        content ={
        'data':data
         }
        return render(request,'products.html',context=content)