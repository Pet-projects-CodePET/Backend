from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from django.contrib.auth import get_user_model

from apps.project.models import FavoriteProject


User = get_user_model()


class FavoriteProjectSerializer(ModelSerializer):
    """Сериализатор избранных проектов"""
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault(),
        required=False
    )

    class Meta:
        model = FavoriteProject
        fields = ("user", "project")
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=FavoriteProject.objects.all(),
                fields=["user", "projects"],
                message="Данный проект уже находится в избранных проектах"
            )
        ]
