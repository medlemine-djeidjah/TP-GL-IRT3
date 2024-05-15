# profiles/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import ProfileUpdateForm, ChangePasswordForm

@login_required
def view_profile(request):
    user = request.user
    profile_data = {
        'name': user.profile.name,
        'phone_number': user.profile.phone_number
    }
    return render(request, 'templates/profile.html', {'profile_data': profile_data})

@login_required
def update_profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('view_profile')
    else:
        form = ProfileUpdateForm(instance=user.profile)
    return render(request, 'templates/profile.html', {'form': form})

@login_required
def change_password(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(user, request.POST)
        if form.is_valid():
            user.set_password(form.cleaned_data['new_password'])
            user.save()
            # Mettre à jour la session de l'utilisateur pour éviter la déconnexion
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been changed successfully.')
            return redirect('view_profile')
    else:
        form = ChangePasswordForm(user)
    return render(request, 'templates/profile.html', {'form': form})

@login_required
def delete_account(request):
    user = request.user
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Your account has been deleted successfully.')
        return redirect('logout')  # Rediriger vers la page de déconnexion après la suppression du compte
    return render(request, 'authentification/templates/logout.html')
