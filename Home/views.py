from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def HomePage(request):
    return render(request,'home.html')
