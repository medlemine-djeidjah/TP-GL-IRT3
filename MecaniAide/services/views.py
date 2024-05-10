
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ServiceRequestForm
from .models import ServiceRequest

@login_required
def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user  # Associer la demande à l'utilisateur
            service_request.save()
            return redirect('service')  # Redirection vers une page de succès
    else:
        form = ServiceRequestForm()

    return render(request, 'service.html', {'form': form})

# Create your views here.
