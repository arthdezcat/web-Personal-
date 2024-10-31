from django.shortcuts import render
from .models import Project, About
# Create your views here.

def portfolio(request):
    projects = Project.objects.all()  
    return render(request, "portfolio/portfolio.html",{'projects':projects})  # <=====

def about(request):
    projectAbouts = About.objects.all()  
    return render(request, "portfolio/about.html",{'projectAbouts':projectAbouts})  # <=====