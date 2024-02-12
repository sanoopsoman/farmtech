from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages,auth
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    return render(request,'index.html')

def farmerregister(request):
    return render(request,'farmerregister.html')

def farmtechregister(request):
    return render(request,'farmtechregister.html')

def login(request):
    return render(request,'login.html')