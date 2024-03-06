from django.shortcuts import render
from about.models import HeaderInfo
from .models import Education, Experience,Skills

# Create your views here.


def resume(request):
    exp = Experience.objects.all()
    edu = Education.objects.all()
    info = HeaderInfo.objects.last()
    skill = Skills.objects.all()
    
    return render(request, 'resume.html', {"info": info, 'edu': edu,'exp':exp,'skill':skill})
