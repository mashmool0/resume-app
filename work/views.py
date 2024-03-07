from django.shortcuts import render
from about.models import HeaderInfo
from .models import Sample 
# Create your views here.


def work(request):
    sample = Sample.objects.all()
    info = HeaderInfo.objects.last()
    return render(request, 'works.html', context={'info': info,'sample':sample})

