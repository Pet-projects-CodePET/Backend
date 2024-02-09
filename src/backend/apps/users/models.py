from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.general.constants import EMAIL_HELP_TEXT, MAX_LENGTH_EMAIL
from apps.general.models import CreatedModifiedFields
from apps.general.validators import CustomEmailValidator
from apps.users.constants import (
    MAX_LENGTH_NICKNAME,
    NICKNAME_ERROR_TEXT,
    NICKNAME_HELP_TEXT,
)


class CustomUserManager(UserManager):
    """Менеджер объектов пользователей."""

    @classmethod
    def normalize_email(cls, email):
        """Нормализация email. Приведение символов к нижнему регистру."""

        try:
            email_name, domain_part = email.strip().rsplit("@", 1)
        except ValueError:
            pass
        else:
            email = f"{email_name.lower()}@{domain_part.lower()}"
        return email


class User(CreatedModifiedFields, AbstractUser):
    """Модель пользователя."""

    date_joined = first_name = last_name = None
    email = models.EmailField(
        max_length=MAX_LENGTH_EMAIL,
        unique=True,
        blank=False,
        help_text=EMAIL_HELP_TEXT,
        validators=[CustomEmailValidator()],
    )
    username = models.CharField(
        _("username"),
        max_length=MAX_LENGTH_NICKNAME,
        unique=True,
        help_text=NICKNAME_HELP_TEXT,
        validators=[UnicodeUsernameValidator()],
        error_messages={
            "unique": NICKNAME_ERROR_TEXT,
        },
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    objects = CustomUserManager()

    class Meta:
        ordering = (
            "created",
            "username",
        )

    def get_full_name(self) -> str:
        """Метод получения полного имени пользователя."""

        return self.username

    def get_short_name(self) -> str:
        """Метод получения сокращенного имени пользователя."""

        return self.username
