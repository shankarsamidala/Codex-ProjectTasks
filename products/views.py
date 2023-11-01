from django.shortcuts import render
from django.http import HttpResponse

def ProductPage(request):
    return render(request, 'products.html')
