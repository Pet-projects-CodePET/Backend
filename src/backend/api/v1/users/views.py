from django.contrib.auth import get_user_model
from djoser.compat import get_user_email
from djoser.conf import settings as dj_settings
from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.v1.users.serializers import CustomUserCreateSerializer


class CustomUserViewSet(UserViewSet):
    """Вьюсет пользователя."""

    queryset = get_user_model().objects.all()

    def activation(self) -> None:
        """Процесс активации отключен."""

    @action(["post"], detail=False)
    def resend_activation(self, request, *args, **kwargs):
        """Повторная отправка сообщения со ссылкой с токеном аутентификации."""

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.get_user()

        if user:
            context = {"user": user}
            to = [get_user_email(user)]
            dj_settings.EMAIL.confirmation(self.request, context).send(to)

        return Response(status=status.HTTP_204_NO_CONTENT)
