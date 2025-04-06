from django.db import models
from django.db import models
from users.models import CustomUser

class Habit(models.Model):
    DAILY = 'daily'
    WEEKLY = 'weekly'

    FREQUENCY_CHOICES = [
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='habits')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default=DAILY)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
