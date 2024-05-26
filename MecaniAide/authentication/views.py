from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import PhoneLoginForm, PhoneRegistrationForm
from django.conf import settings

def login_view(request):
    if request.method == 'POST':
        form = PhoneLoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = authenticate(request, phone_number=phone_number, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid phone number or password')
    else:
        form = PhoneLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page

def register_view(request):
    if request.method == 'POST':
        form = PhoneRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            raw_password = form.cleaned_data.get('password1')
            user.set_password(raw_password)  # Hash the password
            user.save()
            # Authenticate the user
            user = authenticate(request, phone_number=user.phone_number, password=raw_password)
            if user is not None:
                # Log in the user
                login(request, user)
                return redirect('home')  # Redirect to home page after successful registration and login
    else:
        form = PhoneRegistrationForm()
    return render(request, 'register.html', {'form': form})
