from django.shortcuts import render
from about.models import HeaderInfo
from .models import Mail

# Create your views here.


def contact(request):
    if (request.method == "POST"):
        nameContact = request.POST.get('nameContact')
        emailContact = request.POST.get('emailContact')
        messageContact = request.POST.get('messageContact')
        if nameContact and emailContact and messageContact:
            Mail.objects.create(FullName=nameContact,
                                email=emailContact, text=messageContact)
            
            
    
    info = HeaderInfo.objects.last()
    return render(request, 'contact.html', context={'info': info, })
