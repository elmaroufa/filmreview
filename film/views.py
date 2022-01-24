from django.shortcuts import render
from .models import Film

# Create your views here.

def home(request):
    searchTerm = request.GET.get('searchFilm') 
    if searchTerm:
        films = Film.objects.filter(title__icontains=searchTerm)
    else:
        films = Film.objects.all()
    return render(request, 'home.html', {'name': 'ABBO', 'searchTerm': searchTerm, 'films': films})


def about(request):
    return render(request,'about.html')


def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})
