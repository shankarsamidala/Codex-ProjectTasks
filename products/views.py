from django.shortcuts import render
from django.http import HttpResponse
from .models import ProductList

# Create your views here.

def ProductPage(request):

      data = ProductList.objects.all()

      prod = {
            "data":data
      }

      return render(request,'Products.html',context=prod)

