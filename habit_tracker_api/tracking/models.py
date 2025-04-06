from django.db import models
from habits.models import Habit

class HabitRecord(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='records')
    date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=True)

    class Meta:
        unique_together = ['habit', 'date']  # Ensure a habit is only marked once per day

    def __str__(self):
        return f"{self.habit.name} - {self.date} - {'Completed' if self.completed else 'Not Completed'}"
