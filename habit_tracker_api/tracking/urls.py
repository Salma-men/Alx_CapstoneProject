from django.urls import path
from .views import MarkHabitCompleteView
from .views import HabitStreaksView


urlpatterns = [
    path('habits/<int:habit_id>/complete/', MarkHabitCompleteView.as_view(), name='mark-habit-complete'),
    path('streaks/', HabitStreaksView.as_view(), name='habit-streaks'),
]
