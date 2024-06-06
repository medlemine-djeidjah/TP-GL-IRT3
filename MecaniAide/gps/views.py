from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@login_required()
def home(request):
    return render(request, 'home.html', {'user': request.user})




