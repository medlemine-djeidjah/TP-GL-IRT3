from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render , redirect
from django.contrib import messages
from store.models import CarPart, Order
import csv


def upload_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Please upload a CSV file.')
        else:
            handle_uploaded_csv(csv_file)
            messages.success(request, 'CSV file uploaded successfully.')
            return redirect('car_parts_store')  # Redirect to view orders after successful upload
    return render(request, 'upload_csv.html')

def handle_uploaded_csv(csv_file):
    decoded_file = csv_file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)
    for row in reader:
        order_number = row.get('order_number')  # Assuming 'order_number' column exists in CSV
        order, _ = Order.objects.get_or_create(order_number=order_number)
        CarPart.objects.create(
            name=row['name'],
            description=row['description'],
            price=row['price'],
            image_url=row['image_url'],
            order=order
        )

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="orders.csv"'

    writer = csv.writer(response)
    writer.writerow(['Order Number', 'Date Ordered', 'Name', 'Description', 'Price'])

    orders = Order.objects.all()
    for order in orders:
        car_parts = order.car_parts.all()
        for part in car_parts:
            writer.writerow([order.order_number, order.date_ordered, part.name, part.description, part.price])

    return response

