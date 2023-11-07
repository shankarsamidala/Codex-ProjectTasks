from django.shortcuts import render
from .models import Order_List
# Create your views here.
def Order(request):

    data = Order_List.objects.all()

    content = {
      'data':data
    }

    return render(request, 'orders.html', context= content)