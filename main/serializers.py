# serializers.py
from rest_framework import serializers
from .models import Event
from datetime import datetime

class EventSerializer(serializers.ModelSerializer):
    timestamp = serializers.CharField()  # timestamp приходит как строка, будем парсить вручную

    class Meta:
        model = Event
        fields = ['id', 'people_count', 'timestamp', 'image']

    def validate_timestamp(self, value):
        # Преобразуем строку в объект DateTime
        try:
            return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')  # Пример формата: "2024-11-10 15:30:00"
        except ValueError:
            raise serializers.ValidationError("Invalid timestamp format. Expected 'YYYY-MM-DD HH:MM:SS'.")
