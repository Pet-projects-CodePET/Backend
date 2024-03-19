from django.db.models import Q
from rest_framework import generics

from api.v1.profile.permissions import IsOwnerOrReadOnly
from api.v1.profile.serializers import ProfileUpdateSerializer
from apps.profile.models import Profile
from apps.projects.models import Project


class ProfileView(generics.RetrieveAPIView):
    """Представление на изменение данных в профиле"""

    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSerializer
    permisssion_classes = IsOwnerOrReadOnly


class ProfileListAPIView(generics.ListAPIView):
    """Список профилей в зависимости от их видимости"""

    serializer_class = ProfileUpdateSerializer

    def get_queryset(self):
        user = self.request.user
        visible_status = self.request.query_params.get("visible_status", "All")
        is_organizer = (
            user.is_authenticated
            and Project.objects.filter(creator=user).exists()
        )

        if visible_status == "Only creator" and user.is_authenticated:
            # Проверяем, является ли пользователь организатором каких-либо проектов
            if is_organizer:
                queryset = Profile.objects.filter(
                    visible_status__in=["All", "Only creator"]
                )
            else:
                queryset = Profile.objects.filter(
                    visible_status="all"
                )  # Если пользователь не организатор, возвращаем только то, что видно всем
        else:
            queryset = Profile.objects.filter(visible_status="All")

        return queryset
