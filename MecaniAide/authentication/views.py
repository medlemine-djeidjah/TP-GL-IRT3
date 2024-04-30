from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import PhoneLoginForm
from .forms import PhoneRegistrationForm


def login_view(request):
    if request.method == 'POST':
        form = PhoneLoginForm(request, request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = authenticate(request, phone_number=phone_number, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to dashboard or any other page
    else:
        form = PhoneLoginForm(request)
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page


def register_view(request):
    if request.method == 'POST':
        form = PhoneRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = PhoneRegistrationForm()
    return render(request, 'register.html', {'form': form})