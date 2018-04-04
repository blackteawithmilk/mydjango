from django.shortcuts import render

# Create your views here.

# coding: utf-8

def home(request):
    return render(request, 'home.html')