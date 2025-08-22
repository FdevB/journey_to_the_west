from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail

import random

from accounts_app.forms import SignupForm
from accounts_app.decorators import logout_required

# Create your views here.
@logout_required
def signup_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(request, "Your account was created and you are logged in.")

            return redirect('home_app:home')

    return render(request, 'accounts_app/signup.html', {'form': form})

@logout_required
def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            request.session.set_expiry(0)
            if request.POST.get('remember'):
                request.session.set_expiry(2592000) # 30 * 24 * 60 * 60 | 30 days

            if user := authenticate(request, username=username, password=password):
                login(request, user)
                messages.success(request, "Loged in successfuly.")
                return redirect('home_app:home')
            

    return render(request, 'accounts_app/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home_app:home')
