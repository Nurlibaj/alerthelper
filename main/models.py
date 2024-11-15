from django.db import models
from django.core.exceptions import ValidationError

class Restroom(models.Model):
    location = models.CharField(max_length=100, help_text="Расположение туалета, например, 'Коридор 2 этажа'")
    max_capacity = models.PositiveIntegerField(help_text="Максимальное количество людей")
    status = models.BooleanField(default=True,help_text="True - красный, False - зеленый")
    floor = models.PositiveIntegerField(default=1, help_text="Этаж, начиная с 1")

    def __str__(self):
        return f"Restroom at {self.location} on floor {self.floor}"

class Event(models.Model):
    id = models.CharField(max_length=255, primary_key=True)  # уникальный идентификатор (можно строковый)
    people_count = models.IntegerField()  # количество людей
    timestamp = models.DateTimeField()  # дата и время
    image = models.ImageField(upload_to='events_images/', null=True, blank=True)  # изображение

    def __str__(self):
        return f"Event {self.id}"

