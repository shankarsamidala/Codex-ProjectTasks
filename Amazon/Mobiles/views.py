from django.shortcuts import render
from django.http import HttpResponse
from .models import moi
# Create your views here.
def mo(request):
    return HttpResponse('This is amazon')