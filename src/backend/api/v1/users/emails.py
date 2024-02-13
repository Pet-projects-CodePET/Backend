from typing import Dict, Union

from django.views import View as ViewType
from djoser.conf import settings as dj_settings
from djoser.email import BaseEmailMessage, ConfirmationEmail
from rest_framework.authtoken.models import Token

from apps.users.models import User as UserType


class RegistrationConfirmEmail(ConfirmationEmail):
    """Класс отправки email сообщения после завершения регистрации."""

    def get_context_data(self) -> Dict[str, Union[str, UserType, ViewType]]:
        """
        Метод получения контекста для шаблона email о завершении регистрации.
        """

        context = super().get_context_data()

        user = context.get("user")
        context["token"], created = Token.objects.get_or_create(user=user)
        context["url"] = dj_settings.ACTIVATION_URL.format(**context)
        return context


class PasswordResetEmail(BaseEmailMessage):
    """Класс отправки email сообщения с новым паролем пользователя."""

    template_name = "email/password_reset.html"
