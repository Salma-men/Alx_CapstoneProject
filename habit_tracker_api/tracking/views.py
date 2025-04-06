from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from datetime import date


from .models import HabitRecord
from habits.models import Habit
from .serializers import HabitRecordSerializer
from .utils import calculate_streak

class MarkHabitCompleteView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, habit_id):
        try:
            habit = Habit.objects.get(id=habit_id, user=request.user)
        except Habit.DoesNotExist:
            return Response({"error": "Habit not found."}, status=status.HTTP_404_NOT_FOUND)

        # Prevent marking the habit more than once per day
        today = date.today()
        if HabitRecord.objects.filter(habit=habit, date=today).exists():
            return Response({"message": "Habit already marked as completed today."}, status=status.HTTP_400_BAD_REQUEST)

        habit_record = HabitRecord.objects.create(habit=habit)
        serializer = HabitRecordSerializer(habit_record)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class HabitStreaksView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        habits = Habit.objects.filter(user=request.user)
        data = []

        for habit in habits:
            streak = calculate_streak(habit)
            data.append({
                'habit_id': habit.id,
                'habit_name': habit.name,
                'streak': streak,
                'frequency': habit.frequency
            })

        return Response(data)