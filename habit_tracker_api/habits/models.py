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

class HabitTracking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='habit_trackings')
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='trackings')
    date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ['user', 'habit', 'date']  # Ensure one completion per day per habit

    def __str__(self):
        return f"{self.user.username} - {self.habit.name} on {self.date}"