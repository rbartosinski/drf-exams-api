from rest_framework.viewsets import ModelViewSet

from .models import Exam, Task
from .serializers import ExamSerializer, TaskSerializer


class ExamViewSet(ModelViewSet):

    serializer_class = ExamSerializer
    queryset = Exam.objects.all()


class TaskViewSet(ModelViewSet):

    serializer_class = TaskSerializer
    queryset = Task.objects.all()
