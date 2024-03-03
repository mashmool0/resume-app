from django.shortcuts import render
from .models import HeaderInfo 
# Create your views here.


def about(request) : 
    info = HeaderInfo.objects.last()
    return render(request,'about.html',{"info":info})

def resume(request) : 
    info = HeaderInfo.objects.last() 
    return render(request,'resume.html',{"info":info})