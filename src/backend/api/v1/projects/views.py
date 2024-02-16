from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from apps.project.models import Project

from .paginations import CustomPagination
from .serializers import PreviewProjectSerializer, ProjectSerializer


class ProjectViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet
):
    """Обработчик URL-запросов к эндпоинту 'Project'."""

    queryset = Project.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ProjectSerializer
    pagination_class = CustomPagination


class ProjectPreviewViewSet(mixins.ListModelMixin, GenericViewSet):
    """Обработчик URL-запросов к эндпоинту 'project/preview_main'."""

    queryset = Project.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = PreviewProjectSerializer
    pagination_class = CustomPagination
