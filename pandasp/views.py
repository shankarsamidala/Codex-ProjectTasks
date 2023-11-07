from django.shortcuts import render
from django.http import HttpResponse
from pandasp.models import products
# Create your views here.
def product(request):
    
    data=products.objects.all()
    con={
        'data':data
    }
    return render(request,'pandasp.html',context=con)
