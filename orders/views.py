from django.shortcuts import render
from django.http import HttpResponse

def OrderPage(response):
    return HttpResponse('orders page')
