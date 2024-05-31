from django.http import HttpResponse
import csv
from store.models import CarPart  # Assurez-vous d'importer correctement votre modèle CarPart

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
