from rest_framework import serializers
from .models import HabitRecord

class HabitRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitRecord
        fields = ['id', 'habit', 'date', 'completed']
