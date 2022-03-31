from rest_framework import permissions
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from .custom_permissions import IsOwnerOrReadOnly, IsOwnerExamOrReadOnly
from .models import Exam, Task
from .serializers import ExamSerializer, TaskSerializer


class ExamViewSet(ModelViewSet):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    serializer_class = ExamSerializer
    queryset = Exam.objects.all()

    filter_backends = (OrderingFilter,)
    ordering_fields = ('owner', 'final_grade', 'name')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)


class TaskViewSet(ModelViewSet):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerExamOrReadOnly,)

    serializer_class = TaskSerializer
    queryset = Task.objects.all()
