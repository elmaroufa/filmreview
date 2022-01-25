from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect
# Create your views here.

def signupaccount(request):
    return render(request, 'signupaccount.html', {'form': UserCreationForm})

