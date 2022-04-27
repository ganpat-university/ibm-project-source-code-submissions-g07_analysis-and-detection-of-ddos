from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from .forms import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    return redirect('login')

def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def visualization_view(request):
    return render(request, 'visualization_view.html')

@login_required
def input_view(request):
    return render(request, 'input_view.html')
