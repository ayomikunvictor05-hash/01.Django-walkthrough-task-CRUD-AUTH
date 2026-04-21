from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.

from .forms import UserRegistrationForm, LoginForm


def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'auth/register.html', {'form':form})


def login_user(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        # form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.user
            login(request, user)             
    return render(request, 'auth/login.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')

