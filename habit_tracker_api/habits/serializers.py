from rest_framework import serializers
from .models import Habit
from .models import HabitTracking


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['id', 'name', 'description', 'frequency', 'created_at']

class HabitTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitTracking
        fields = ['id', 'habit', 'date', 'completed']