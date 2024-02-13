from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from djoser.compat import get_user_email
from djoser.conf import settings as dj_settings
from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from api.v1.users.constants import (
    NEW_PASSWORD_ALLOWED_CHARS,
    NEW_PASSWORD_LENGTH,
)
from api.v1.users.utils import get_user_from_request


class CustomUserViewSet(UserViewSet):
    """Вьюсет пользователя."""

    queryset = get_user_model().objects.all()

    def activation(self) -> None:
        """Процесс активации отключен."""

    def reset_password_confirm(self) -> None:
        """Процесс подтверждения сброса пароля отключен."""

    def set_username(self) -> None:
        """Процесс установки username пользователя отключен."""

    def reset_username(self) -> None:
        """Процесс сброса username пользователя отключен."""

    def reset_username_confirm(self) -> None:
        """Процесс подтверждения сброса username пользователя отключен."""

    @action(["post"], detail=False)
    def resend_activation(self, request, *args, **kwargs) -> Response:
        """Повторная отправка сообщения со ссылкой с токеном аутентификации."""

        user = get_user_from_request(self)

        if user is not None:
            context = {"user": user}
            dj_settings.EMAIL.confirmation(
                self.request,
                context,
            ).send([get_user_email(user)])

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(["post"], detail=False)
    def reset_password(self, request, *args, **kwargs):
        """Сброс пароля с отправкой нового на почту."""

        user = get_user_from_request(self)

        if user is not None:
            new_password = get_random_string(
                length=NEW_PASSWORD_LENGTH,
                allowed_chars=NEW_PASSWORD_ALLOWED_CHARS,
            )
            user.set_password(new_password)
            user.save()
            context = {"user": user}
            context["new_password"] = new_password
            dj_settings.EMAIL.password_reset(
                self.request,
                context,
            ).send([get_user_email(user)])

        return Response(status=status.HTTP_204_NO_CONTENT)
