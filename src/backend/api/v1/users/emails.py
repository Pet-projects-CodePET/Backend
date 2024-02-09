from djoser.conf import settings as dj_settings
from djoser.email import ConfirmationEmail
from rest_framework.authtoken.models import Token


class TokenEmail(ConfirmationEmail):
    """
    Класс отправки email сообщения со ссылкой с токеном для аутентификации.
    """

    def get_context_data(self):
        """Метод получения контекста для шаблона email."""

        context = super().get_context_data()

        user = context.get("user")
        context["token"], created = Token.objects.get_or_create(user=user)
        context["url"] = dj_settings.ACTIVATION_URL.format(**context)
        return context
