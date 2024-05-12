from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserLocation
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


#@login_required(login_url= "auth/login/")
def home(request):
    return render(request, 'home.html', {'user': request.user})


#@login_required
@csrf_exempt
def update_location(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        
        # Assuming you have authenticated users
        user = request.user
        
        UserLocation.objects.create(user=user, latitude=latitude, longitude=longitude)
        
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})