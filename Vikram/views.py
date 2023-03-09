from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Hero(request):
    return HttpResponse('<h2>Kamal_Hassan</h2> is the <h3>Hero</h3> ')

def Villain(request):
    return HttpResponse('<h2>Rolex is the Villain</h2>')

def Heroine(request):
    return HttpResponse('<h3>Heroine is Unknown</h3>')