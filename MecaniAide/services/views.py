# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ServiceRequest, ServiceResponse
from .forms import ServiceRequestForm, ServiceStatusUpdateForm, ServiceResponseForm
from django.contrib.auth.models import User

def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            technician_type = form.cleaned_data.get('technician_type')

            if technician_type == 'mechanic':
                technician = User.objects.filter(groups__name='Mechanic').first()
            elif technician_type == 'electrician':
                technician = User.objects.filter(groups__name='Electrician').first()
            else:
                technician = None

            if technician:
                service_request.technician = technician

            service_request.save()
            return redirect('service')
    else:
        form = ServiceRequestForm()
    return render(request, 'service.html', {'form': form})

@login_required
def update_service_status(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    if request.method == 'POST':
        form = ServiceStatusUpdateForm(request.POST, instance=service_request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service status updated successfully.')
            return redirect('service_detail', request_id=service_request.id)
    else:
        form = ServiceStatusUpdateForm(instance=service_request)
    return render(request, 'update_status.html', {'form': form, 'service_request': service_request})

@login_required
def add_service_response(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    if request.method == 'POST':
        form = ServiceResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.service_request = service_request
            response.responder = request.user
            response.save()
            messages.success(request, 'Response added successfully.')
            return redirect('service_detail', request_id=service_request.id)
    else:
        form = ServiceResponseForm()
    return render(request, 'add_response.html', {'form': form, 'service_request': service_request})
