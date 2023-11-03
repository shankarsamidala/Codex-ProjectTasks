from django.shortcuts import render
from django.http import HttpResponse


def product(request):
    return render(request,'products.html')

# Create your views here.
