from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ServiceProviderProfile, Region

@login_required()
def home(request):
    return render(request, 'home.html', {'user': request.user})






def service_providers_map(request):
    regions = Region.objects.all()
    service_providers = ServiceProviderProfile.objects.all()
    return render(request, 'service_providers_map.html', {
        'regions': regions,
        'service_providers': service_providers
    })
