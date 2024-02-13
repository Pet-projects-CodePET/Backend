from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from apps.project.models import Project

from .paginations import CustomPagination
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """Обработчик URL-запросов к эндпоинту 'Project'."""

    queryset = Project.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ProjectSerializer
    pagination_class = CustomPagination
