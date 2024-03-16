from django.db.models import Prefetch
from rest_framework import mixins
from rest_framework.permissions import (
    SAFE_METHODS,
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.viewsets import (
    GenericViewSet,
    ModelViewSet,
    ReadOnlyModelViewSet,
)

from api.v1.projects.paginations import (
    ProjectPagination,
    ProjectPreviewMainPagination,
)
from api.v1.projects.serializers import (
    DirectionSerializer,
    ProjectPreviewMainSerializer,
    ReadProjectSerializer,
    WriteProjectSerializer,
)
from apps.projects.models import Direction, Project, ProjectSpecialist


class DirectionViewSet(ReadOnlyModelViewSet):
    """Представление направлений разработки."""

    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = (IsAuthenticated,)


class ProjectViewSet(ModelViewSet):
    """Представление проектов."""

    queryset = Project.objects.select_related(
        "creator", "owner"
    ).prefetch_related(
        Prefetch(
            "project_specialists",
            queryset=ProjectSpecialist.objects.select_related(
                "specialist"
            ).prefetch_related("skills"),
        ),
        "directions",
    )
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = ProjectPagination

    def get_serializer_class(self):
        """Метод получения сериализатора проектов."""

        if self.request.method in SAFE_METHODS:
            return ReadProjectSerializer
        return WriteProjectSerializer

    def perform_create(self, serializer):
        """Метод предварительного создания объекта."""

        user = self.request.user
        serializer.save(creator=user, owner=user)


class ProjectPreviewMainViewSet(mixins.ListModelMixin, GenericViewSet):
    """Представление превью проектов на главной странице."""

    queryset = (
        Project.objects.exclude(status=Project.DRAFT)
        .only(
            "id",
            "name",
            "started",
            "ended",
            "directions",
        )
        .prefetch_related(
            Prefetch(
                "project_specialists",
                queryset=ProjectSpecialist.objects.select_related(
                    "specialist"
                ),
            ),
            "directions",
        )
    )
    permission_classes = (AllowAny,)
    serializer_class = ProjectPreviewMainSerializer
    pagination_class = ProjectPreviewMainPagination
