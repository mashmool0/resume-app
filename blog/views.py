from django.shortcuts import render
from about.models import HeaderInfo
from .models import Blog_post
# Create your views here.


def blog(request):
    blog = Blog_post.objects.all()
    info = HeaderInfo.objects.last()
    return render(request, 'blog.html', context={'info': info, 'blog': blog})


def post(request, poster):
    info = HeaderInfo.objects.last()
    blog_post = Blog_post.objects.all()
    for item in blog_post:
        if item.randomkey == poster:
            return render(request, 'single-post.html', context={'info': info, 'blog_post': blog_post, })
