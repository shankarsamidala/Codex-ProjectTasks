from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app(request):
    return HttpResponse("this is app1")
def chai(request):
    return render(request,'index.html')