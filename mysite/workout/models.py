from django.db import models

INTENSITY_CHOICES = [
    (0, 'Нет данных'),
    (1, 'Лёгкая'),
    (2, 'Средняя'),
    (3, 'Хорошая'),
    (4, 'Интенсивная'),
]

class Training(models.Model):
    date = models.DateField()
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    intensity = models.PositiveSmallIntegerField(
        choices=INTENSITY_CHOICES,
        default=0
    )