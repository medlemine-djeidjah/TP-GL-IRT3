from django.shortcuts import render

# Create your views here.

import csv
from django.http import HttpResponse
from .models import DemandeAssistance

def export_demandes_assistance(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="demandes_assistance.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Date de création', 'Statut', 'Type d\'incident', 'Description', 'Client'])

    demandes_assistance = DemandeAssistance.objects.all()
    for demande in demandes_assistance:
        writer.writerow([demande.id, demande.date_creation, demande.statut, demande.type_incident, demande.description, demande.client])

    return response