from django.urls import path
from .views import MarkHabitCompleteView
from .views import HabitStreaksView
from .views import HabitCompletionRateView


urlpatterns = [
    path('habits/<int:habit_id>/complete/', MarkHabitCompleteView.as_view(), name='mark-habit-complete'),
    path('streaks/', HabitStreaksView.as_view(), name='habit-streaks'),
    path('completion-rates/', HabitCompletionRateView.as_view(), name='habit-completion-rate'),  # New route

]
