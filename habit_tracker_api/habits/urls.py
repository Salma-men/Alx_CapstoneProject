from django.urls import path
from .views import HabitListCreateView, HabitDetailView, MarkHabitCompletedView, HabitMarkIncompleteView, CompletedHabitsTodayView

urlpatterns = [
    path('', HabitListCreateView.as_view(), name='habit-list-create'),
    path('<int:pk>/', HabitDetailView.as_view(), name='habit-detail'),
    path('<int:pk>/complete/', MarkHabitCompletedView.as_view(), name='habit-mark-completed'),
    path('<int:habit_id>/incomplete/', HabitMarkIncompleteView.as_view(), name='habit-incomplete'),
    path('completed/', CompletedHabitsTodayView.as_view(), name='habits-completed-today'),

]
