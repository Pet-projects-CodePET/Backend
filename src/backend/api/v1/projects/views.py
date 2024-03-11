from django.db.models import Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from apps.project.models import Project, ProjectSpecialist

from .filters import ProjectFilter
from .constants import PROJECT_PREVIEW_MAIN_FIELDS
from .paginations import ProjectPagination, ProjectPreviewMainPagination
from .serializers import ProjectPreviewMainSerializer, ProjectSerializer


class ProjectViewSet(ModelViewSet):
    """Представление проектов."""

    queryset = (
        Project.objects.all()
        .select_related("creator", "owner")
        .prefetch_related(
            Prefetch(
                "project_specialists",
                queryset=ProjectSpecialist.objects.select_related(
                    "specialist__specialization"
                ).prefetch_related("skills"),
            ),
        )
    )
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ProjectSerializer
    pagination_class = ProjectPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProjectFilter


class ProjectPreviewMainViewSet(mixins.ListModelMixin, GenericViewSet):
    """Представление превью проектов на главной странице."""

    queryset = (
        Project.objects.all()
        .only(*PROJECT_PREVIEW_MAIN_FIELDS)
        .prefetch_related(
            Prefetch(
                "project_specialists",
                queryset=ProjectSpecialist.objects.select_related(
                    "specialist__specialization"
                ),
            )
        )
    )
    permission_classes = (AllowAny,)
    serializer_class = ProjectPreviewMainSerializer
    pagination_class = ProjectPreviewMainPagination
