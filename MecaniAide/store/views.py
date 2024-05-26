from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

from .models import CarPart

def car_parts_store(request):
    return render(request, 'store.html')

def car_parts_store_api(request):
    parts = CarPart.objects.all().values('id', 'name', 'description', 'price', 'image_url')
    return JsonResponse(list(parts), safe=False)