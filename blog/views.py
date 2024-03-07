from django.shortcuts import render
from about.models import HeaderInfo 
from .models import Blog_post
# Create your views here.


def blog(request) : 
    blog = Blog_post.objects.all() 
    info = HeaderInfo.objects.last() 
    return render(request,'blog.html',context={'info':info,'blog':blog})