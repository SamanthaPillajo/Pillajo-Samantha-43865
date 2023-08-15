from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    return render(request,'aplicacion/base.html')

def tops(request):
    return render(request, "aplicacion/tops.html")

def bottoms(request):
    return render(request, "aplicacion/bottoms.html")

def shoes(request):
    return render(request, "aplicacion/shoes.html")

def accesories(request):
    return render(request, "aplicacion/accesories.html")

