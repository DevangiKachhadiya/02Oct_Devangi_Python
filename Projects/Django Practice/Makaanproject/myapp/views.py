from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def property_agent(request):
    return render(request,'property-agent.html')

def property_list(request):
    return render(request,'property-list.html')

def property_type(request):
    return render(request,'property-type.html')

def testimonial(request):
    return render(request,'testimonial.html')
