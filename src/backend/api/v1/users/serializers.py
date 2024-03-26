from django.contrib.auth import get_user_model
from djoser.serializers import (
    SendEmailResetSerializer,
    UserCreatePasswordRetypeSerializer,
    UserSerializer,
)
from rest_framework import serializers

from api.v1.users import constants

User = get_user_model()


class CustomUserSerializer(UserSerializer):
    """Сериализатор пользователя."""

    class Meta(UserSerializer.Meta):
        fields = constants.ORDERED_USERS_FIELDS


class CustomUserCreateSerializer(UserCreatePasswordRetypeSerializer):
    """Сериализатор для регистрации пользователя с подтверждением пароля."""

    class Meta(UserCreatePasswordRetypeSerializer.Meta):
        fields = constants.ORDERED_USERS_FIELDS + ("password",)
