from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def basic(request):
    return render(request,'basic.html')

def doctor(request):
    doctors = [
        {
            'name': 'Dr. Vivek Kachhadiya',
            'specialization': 'Cardiology (Heart Specialist)',
            'experience': '15 years',
            'hospital': 'City Health Hospital',
            'contact': '+1234567890',
            'email': 'johndoe@example.com',
        },
        {
            'name': 'Dr. Devangi Kachhadiya',
            'specialization': 'Neurology (Brain Specialist)',
            'experience': '10 years',
            'hospital': 'Neuro Care Clinic',
            'contact': '+9876543210',
            'email': 'janesmith@example.com',
        },
        {
            'name': 'Dr. Bindiya Mendapara',
            'specialization': 'Pediatrics (Child Specialist)',
            'experience': '8 years',
            'hospital': 'Happy Kids Hospital',
            'contact': '+1122334455',
            'email': 'emilybrown@example.com',
        }
    ]
    return render(request, 'doctor.html', {'doctors': doctors})
