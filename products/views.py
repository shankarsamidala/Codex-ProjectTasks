from django.shortcuts import render
from django.http import HttpResponse
def Productpage(request):
    return render(request,'products.html')