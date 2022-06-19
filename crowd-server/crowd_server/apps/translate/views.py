from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculate():
    x = 1
    y = 2
    return(x+y)

def say_hello(request):
    x = calculate()
    return render(request,'hello.html')
    #return render(request,'hello.html',{'name':'fatemeh'})

