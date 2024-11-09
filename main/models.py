from django.db import models
from django.core.exceptions import ValidationError

class Restroom(models.Model):
    id=models.AutoField(primary_key=True)
    location = models.CharField(max_length=100, help_text="Расположение туалета, например, 'Коридор 2 этажа'")
    max_capacity = models.PositiveIntegerField(help_text="Максимальное количество людей")
