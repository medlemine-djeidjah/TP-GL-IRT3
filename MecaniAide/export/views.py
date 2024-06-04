<<<<<<< HEAD
from django.http import HttpResponse
import csv
from .models import CarPart  # Assurez-vous d'importer correctement votre modèle CarPart

def export_csv(request):
    # Récupérer toutes les pièces de voiture de la base de données
    car_parts = CarPart.objects.all()

    # Créer une réponse HTTP avec le type MIME pour un fichier CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="car_parts.csv"'

    # Créer un écrivain CSV
    writer = csv.writer(response)

    # Écrire l'en-tête du fichier CSV
    writer.writerow(['Name', 'Description', 'Price', 'Image URL'])

    # Écrire les données des pièces de voiture dans le fichier CSV
    for car_part in car_parts:
        writer.writerow([car_part.name, car_part.description, car_part.price, car_part.image_url])

    return response
=======
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
>>>>>>> 5dc325a283b77d22535eae61e57aa24aaa759670
