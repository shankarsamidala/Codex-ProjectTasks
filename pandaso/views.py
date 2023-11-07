from django.shortcuts import render
from django.http import HttpResponse
from pandasp.models import products
from pandaso.models import orders
# Create your views here.
def order(request):
    data=orders.objects.all()
    con={
        'data':data
    }
    return render(request,'pandaso.html',context=con)

   