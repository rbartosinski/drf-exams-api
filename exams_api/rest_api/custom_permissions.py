from rest_framework import permissions
from .models import Exam


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user


class IsOwnerExamOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        exam = Exam.objects.get(id=obj.exam.id)
        if request.method in permissions.SAFE_METHODS:
            return True

        return exam.owner == request.user
