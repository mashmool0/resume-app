from django.shortcuts import render
from about.models import HeaderInfo 
# Create your views here.


def blog(request) : 
    info = HeaderInfo.objects.last() 
    return render(request,'blog.html',context={'info':info,})