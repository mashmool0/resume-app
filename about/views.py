from django.shortcuts import render
from .models import HeaderInfo,WhatToDo,AboutMe 
# Create your views here.


def about(request) : 
    info = HeaderInfo.objects.last()
    whattodo = WhatToDo.objects.last()
    aboutme = AboutMe.objects.last()
    return render(request,'about.html',{"info":info,"whattodo":whattodo,"aboutme":aboutme})

def resume(request) : 
    info = HeaderInfo.objects.last() 
    return render(request,'resume.html',{"info":info})