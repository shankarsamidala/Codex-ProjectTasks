from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ProductList(request):
    return render(request,'Products.html')