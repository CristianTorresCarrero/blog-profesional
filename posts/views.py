from django.shortcuts import render
from .models import Profile


# Create your views here.

def home(request):
    information = Profile.objects.first()
    return render(request, 'sections/home.html', {'information': information})

def projects(request):
    return render(request, 'sections/projects.html')

def studies(request):
    return render(request, 'sections/studies.html')

def hability(request):
    return render(request, 'sections/hability.html')

def contact(request):
    return render(request, 'sections/contact.html')
