from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def newadmission(request):
    return HttpResponse("Admissions are closing soon, Hurryup!.")
def checkadmission(request):
    return HttpResponse("Congratualtions, Your Admission was confrimed.")