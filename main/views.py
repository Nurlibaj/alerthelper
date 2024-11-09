from django.http import HttpResponse
from django.shortcuts import render
from .models import Restroom
from collections import defaultdict


def hello_world(request):
    return HttpResponse("hello")
def index(request):
    # Retrieve all restrooms from the database
    first_floor_restrooms = Restroom.objects.filter(floor=1)
    second_floor_restrooms = Restroom.objects.filter(floor=2)
    third_floor_restrooms = Restroom.objects.filter(floor=3)


    return render(request, 'main/index.html', {
            'first_floor_restrooms': first_floor_restrooms,
            'second_floor_restrooms': second_floor_restrooms,
            'third_floor_restrooms': third_floor_restrooms,
        })