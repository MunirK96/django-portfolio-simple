from django.shortcuts import render
from .models import project

def home(request):
    Projects = project.objects.all()
    return render(request, 'home.html', {'Projects': Projects})
