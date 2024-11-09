def clean(self):
    # Проверяем, что текущее количество людей не превышает максимальное
    if self.current_occupancy > self.max_capacity:
        raise ValidationError('Текущее количество людей не может превышать максимальную вместимость.')


def is_over_capacity(self):
    # Проверка на превышение количества людей
    return self.current_occupancy > self.max_capacity


def _str_(self):
    return f"{self.location} (Максимум: {self.max_capacity}, Сейчас: {self.current_occupancy})"