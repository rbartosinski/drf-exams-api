from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import NestedRouterMixin

from rest_api.views import ExamViewSet, TaskViewSet


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()
exams_router = router.register('exams', ExamViewSet)
exams_router.register(
    'tasks', TaskViewSet,
    basename='exams-tasks',
    parents_query_lookups=['exam']
)

# tasks_router = router.register('tasks', TaskViewSet)
