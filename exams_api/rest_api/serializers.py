from rest_framework import serializers

from .models import Exam, Task


class ExamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exam
        fields = ("id", "name", "description", "final_grade", "owner")


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ("id", "name", "description", "exam", "points")
