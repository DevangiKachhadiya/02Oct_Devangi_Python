from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')

def signUp(request):
    return render(request,'signUp.html')
