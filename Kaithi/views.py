from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Hero(request):
    return HttpResponse('<h5>Karthi</h5> is the <h5>Hero</h5>')

def Villain(request):
    return HttpResponse('<h3>Arjun_Dass is the Villain</h3>')

def Heroine(request):
    return HttpResponse('<h3>Heroine is Unknown</h3>')