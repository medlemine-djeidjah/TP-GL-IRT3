from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import AssistanceRequest
from django.http import JsonResponse
from requests.models import AssistanceMedia
from .forms import AssistanceRequestForm, AssistanceMediaForm
from django.contrib.auth.decorators import user_passes_test



@login_required
def submit_request(request):
    if request.method == 'POST':
        request_form = AssistanceRequestForm(request.POST)
        media_form = AssistanceMediaForm(request.POST, request.FILES)
        
        if request_form.is_valid():
            assistance_request = request_form.save(commit=False)
            assistance_request.user = request.user
            assistance_request.latitude = request.POST.get('latitude')
            assistance_request.longitude = request.POST.get('longitude')
            assistance_request.save()

            for file in request.FILES.getlist('media'):
                AssistanceMedia.objects.create(assistance_request=assistance_request, media=file)
            
            messages.success(request, 'Your request has been submitted successfully!')
            return redirect('submit_request')
    else:
        request_form = AssistanceRequestForm()
        media_form = AssistanceMediaForm()
    
    return render(request, 'submit_request.html', {'request_form': request_form, 'media_form': media_form})

def service_provider_requests(request):
    # Get requests assigned to the current service provider
    assigned_requests = AssistanceRequest.objects.filter(forwarded_to=request.user)
    return render(request, 'service_provider_requests.html', {'assigned_requests': assigned_requests})

def track_request(request, request_id):
    # Render the page with the request_id
    return render(request, 'track_request.html', {'request_id': request_id})

def get_request_details(request, request_id):
    assistance_request = get_object_or_404(AssistanceRequest, pk=request_id)
    data = {
        'user': assistance_request.user.username,
        'description': assistance_request.description,
        'payment_method': assistance_request.payment_method,
        'assistance_type': assistance_request.assistance_type,
        'latitude': assistance_request.latitude,
        'longitude': assistance_request.longitude,
        'created_at': assistance_request.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        'media': [media.media.url for media in assistance_request.media.all()],
    }
    return JsonResponse(data)

def delete_request(request, request_id):
    # Retrieve the requested assistance request
    assistance_request = get_object_or_404(AssistanceRequest, pk=request_id)

    # Delete the request
    assistance_request.delete()

    return redirect('service_provider_requests')