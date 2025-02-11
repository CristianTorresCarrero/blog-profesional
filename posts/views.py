from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'sections/home.html')

def about(request):
    return render(request, 'sections/about.html')

def projects(request):
    return render(request, 'sections/projects.html')

def studies(request):
    return render(request, 'sections/studies.html')

def posts(request):
    return render(request, 'sections/posts.html')

def contact(request):
    return render(request, 'sections/contact.html')
