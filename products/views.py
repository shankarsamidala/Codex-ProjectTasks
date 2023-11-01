from django.shortcuts import render
from django.http import HttpResponse
from .models import productlist
# Create your views here.
def productlist(request):
    return render(request,'products.html')
