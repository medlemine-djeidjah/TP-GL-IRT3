from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserLocation
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'home.html', {'user': request.user})


def tracking(request):
    return render(request, 'tracking.html', {'user': request.user})

