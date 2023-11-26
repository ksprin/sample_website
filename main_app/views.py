from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "main_app/home.html")

def skills(request):
    return render(request, "main_app/skills.html")

def right(request):
    return render(request, "main_app/right.html")
    