from django.shortcuts import render
from .models import HeaderInfo, WhatToDo, AboutMe, Comments
# Create your views here.


def about(request):
    info = HeaderInfo.objects.last()
    whattodo = WhatToDo.objects.all()
    aboutme = AboutMe.objects.last()
    comment = Comments.objects.count()
    if comment != 0:
        comment = Comments.objects.all()
    
    
    return render(request, 'about.html', {"info": info, "whattodo": whattodo, "aboutme": aboutme, "comment": comment})


