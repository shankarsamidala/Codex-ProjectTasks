from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ProductPage(request):
    return render(request, 'product.html')
def HomePage(request):
    return render(request,'home.html')
