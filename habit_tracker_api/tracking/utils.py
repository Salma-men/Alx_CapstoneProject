from datetime import timedelta, date
from habits.models import HabitTracking

def calculate_streak(habit):
    today = date.today()
    frequency = habit.frequency

    if frequency == 'daily':
        delta = timedelta(days=1)
    elif frequency == 'weekly':
        delta = timedelta(weeks=1)
    else:
        return 0

    streak = 0
    current_date = today

    while HabitTracking.objects.filter(habit=habit, date=current_date, completed=True).exists():
        streak += 1
        current_date -= delta

    return streak
