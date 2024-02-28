from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from apps.project.models import FavoriteProject
from api.v1.projects.serializers import FavoriteProjectSerializer


class FavoriteViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, GenericViewSet
):
    """Вьюсет избранных проектов"""

    queryset = FavoriteProject.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = FavoriteProjectSerializer
