from django.http import HttpResponse
from django.shortcuts import render
from .models import Restroom
from collections import defaultdict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializers import EventSerializer
from rest_framework.parsers import MultiPartParser, FormParser


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

class EventCreateView(APIView):
    parser_classes = (MultiPartParser, FormParser)  # Для обработки файлов (изображений) и данных формы

    def post(self, request, *args, **kwargs):
        # Получаем данные из запроса
        serializer = EventSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()  # Сохраняем данные в базе данных
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)