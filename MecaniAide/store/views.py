from django.shortcuts import render

# Create your views here.

from .models import CarPart

def car_parts_store(request):
    parts = CarPart.objects.all()
    return render(request, 'store.html', {'parts': parts})
