from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Habit
from .serializers import HabitSerializer
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Habit, HabitTracking
from .serializers import HabitTrackingSerializer
from rest_framework.permissions import IsAuthenticated
import datetime
from datetime import date


class HabitListCreateView(generics.ListCreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class HabitDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

class MarkHabitCompletedView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        habit = Habit.objects.filter(id=pk, user=request.user).first()

        if not habit:
            return Response({"detail": "Habit not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if the habit has already been completed today
        today = datetime.date.today()
        existing_tracking = HabitTracking.objects.filter(user=request.user, habit=habit, date=today).first()

        if existing_tracking:
            return Response({"detail": "Habit already completed today."}, status=status.HTTP_400_BAD_REQUEST)

        # Mark the habit as completed
        habit_tracking = HabitTracking.objects.create(
            user=request.user,
            habit=habit,
            date=today,
            completed=True
        )

        return Response(HabitTrackingSerializer(habit_tracking).data, status=status.HTTP_201_CREATED)

class HabitMarkIncompleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, habit_id):
        try:
            habit = Habit.objects.get(id=habit_id, user=request.user)
        except Habit.DoesNotExist:
            return Response({"detail": "Habit not found."}, status=status.HTTP_404_NOT_FOUND)

        today = date.today()
        try:
            tracking_entry = HabitTracking.objects.get(habit=habit, date=today)
            tracking_entry.delete()
            return Response({"detail": "Habit marked as incomplete for today."}, status=status.HTTP_200_OK)
        except HabitTracking.DoesNotExist:
            return Response({"detail": "Habit was not completed today."}, status=status.HTTP_400_BAD_REQUEST)

class CompletedHabitsTodayView(generics.ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        today = date.today()
        completed_tracking = HabitTracking.objects.filter(
            habit__user=self.request.user,
            date=today
        ).values_list('habit_id', flat=True)

        return Habit.objects.filter(id__in=completed_tracking)