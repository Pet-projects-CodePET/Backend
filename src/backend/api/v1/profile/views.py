from rest_framework import generics, status
from rest_framework.response import Response

from api.v1.profile.serializers import ProfileUpdateSerializer
from apps.profile.models import Profile


class ProfileView(generics.RetrieveAPIView):
    """Представление на изменение данных в профиле"""

    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSerializer

    def retrieve(self, request, *args, **kwargs):
        profile = self.get_object()
        if profile.user != request.user:
            return Response(
                {"error": "Недостаточно прав доступа"},
                status=status.HTTP_403_FORBIDDEN,
            )
        serializer = self.get_serializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
