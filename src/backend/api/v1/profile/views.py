from rest_framework import generics, status
from rest_framework.response import Response

from api.v1.profile.permissions import IsOwnerOrReadOnly
from api.v1.profile.serializers import ProfileUpdateSerializer
from apps.profile.models import Profile


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
        visibile_status = self.request.query_params.get(
            "visibile_status", "all"
        )
        if visibile_status == "all":
            queryset = Profile.objects.all()
        elif visibile_status == "creator":
            queryset = Profile.objects.filter(
                visibility="creator"
            )  # Выводится в списке, если стоит видимость всем или организаторам проекта
        else:
            queryset = (
                Profile.objects.none()
            )  # Пустой queryset, если не выбраны организаторы
        return queryset
