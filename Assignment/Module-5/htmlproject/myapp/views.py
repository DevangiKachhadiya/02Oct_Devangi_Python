from django.shortcuts import render

# Create your views here.

def html1(request):
    return render(request,'html1.html')

def jango(request):
    return render(request,'jango.html')

def doctor(request):
    return render(request,'doctor.html')

