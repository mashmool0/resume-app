from django.shortcuts import render

# Create your views here.

def work(request) : 
    return render(request,'works.html')
    