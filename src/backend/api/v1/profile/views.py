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
