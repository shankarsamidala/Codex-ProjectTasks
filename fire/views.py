from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sati(request):
    return HttpResponse('I am God')

def mercury(request):
    return HttpResponse('No one can do the job, But I wont agree with that')
