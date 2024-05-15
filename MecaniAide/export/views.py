from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib import messages
from store.models import CarPart
import csv
from io import TextIOWrapper


def upload_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Please upload a CSV file.')
        else:
            handle_uploaded_csv(csv_file)
            messages.success(request, 'CSV file uploaded successfully.')
    return render(request, 'upload_csv.html')



def handle_uploaded_csv(csv_file):
    decoded_file = csv_file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)
    for row in reader:
        CarPart.objects.create(
            name=row['name'],
            description=row['description'],
            price=row['price'],
            image_url=row['image_url']
        )