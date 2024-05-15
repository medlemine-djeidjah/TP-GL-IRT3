
from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from django.contrib.auth.models import User

def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user  # Associer la demande à l'utilisateur

            # Récupérer le type de technicien requis à partir du formulaire
            technician_type = form.cleaned_data.get('technician_type')

            # Trouver un utilisateur avec le rôle de technicien approprié
            if technician_type == 'Mechanic':
                technician = User.objects.filter(groups__name='Mechanic').first()
            elif technician_type == 'Electrician':
                technician = User.objects.filter(groups__name='Electrician').first()
            else:
                technician = None

            if technician:
                # Attribuer la demande de service au technicien trouvé
                service_request.technician = technician

            service_request.save()
            return redirect('home')  # Redirection vers une page de succès
    else:
        form = ServiceRequestForm()

    return render(request, 'service.html', {'form': form})

# Create your views here.
