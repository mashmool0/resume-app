from django.shortcuts import render
from about.models import HeaderInfo
# Create your views here.


def work(request):
    info = HeaderInfo.objects.last()
    return render(request, 'works.html', context={'info': info})
