from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from .forms import UserForm, UserProfileForm, EmailForm, CustomPasswordChangeForm
from .models import UserProfile
from django.contrib.auth import update_session_auth_hash

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        user_form = UserForm(instance=request.user)
        profile_form, created = UserProfile.objects.get_or_create(user=request.user)
        profile_form = UserProfileForm(instance=profile_form)
        email_form = EmailForm(instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user)
        return render(request, 'profile.html', {
            'user_form': user_form,
            'profile_form': profile_form,
            'email_form': email_form,
            'password_form': password_form
        })

    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)
        profile_form, created = UserProfile.objects.get_or_create(user=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile_form)
        email_form = EmailForm(request.POST, instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)

        if 'update_profile' in request.POST and user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        elif 'update_email' in request.POST and email_form.is_valid():
            email_form.save()
            messages.success(request, 'Email updated successfully!')
            return redirect('profile')
        elif 'update_password' in request.POST and password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')

        return render(request, 'profile.html', {
            'user_form': user_form,
            'profile_form': profile_form,
            'email_form': email_form,
            'password_form': password_form
        })
