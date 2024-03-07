from django.shortcuts import render
from about.models import HeaderInfo 
# Create your views here.


def contact(request):
    info = HeaderInfo.objects.last()
    return render(request,'contact.html',context={'info':info,})