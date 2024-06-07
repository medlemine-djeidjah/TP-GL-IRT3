from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import AssistanceRequest
from django.http import JsonResponse
from requests.models import AssistanceMedia
from .forms import AssistanceRequestForm, AssistanceMediaForm
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Count

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

from django.db.models import Count, Sum
from store.models import Order , CarPart

import json
from decimal import Decimal
from django.core.serializers.json import DjangoJSONEncoder

class CustomJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)  # or str(obj)
        return super().default(obj)

@login_required
def assistance_stats(request):
    # Count the number of assistance requests by type
    assistance_by_type = list(AssistanceRequest.objects.values('assistance_type').annotate(total=Count('assistance_type')).order_by('assistance_type'))

    # Count the number of assistance requests by payment method
    payment_by_method = list(AssistanceRequest.objects.values('payment_method').annotate(total=Count('payment_method')).order_by('payment_method'))

    # Retrieve data for orders
    orders_data = list(Order.objects.values('order_number').annotate(total_price=Sum('order_items__total_price')).order_by('order_number'))

    # Retrieve data for car parts
    car_parts_data = list(CarPart.objects.values('name', 'price'))

    return render(request, 'assistance_stats.html', {
        'assistance_by_type': json.dumps(assistance_by_type, cls=CustomJSONEncoder),
        'payment_by_method': json.dumps(payment_by_method, cls=CustomJSONEncoder),
        'orders_data': json.dumps(orders_data, cls=CustomJSONEncoder),
        'car_parts_data': json.dumps(car_parts_data, cls=CustomJSONEncoder)
    })