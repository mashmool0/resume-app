from django.shortcuts import render
from about.models import HeaderInfo 

# Create your views here.


def resume(request):
    info = HeaderInfo.objects.last()
    return render(request, 'resume.html', {"info": info})
