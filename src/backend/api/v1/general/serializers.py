from rest_framework import serializers

from apps.general.models import Skill, Specialization


class SpecializationSerializer(serializers.ModelSerializer):
    """Сериализатор специализации."""

    class Meta:
        model = Specialization
        fields = ("id", "name")


class SkillSerializer(serializers.ModelSerializer):
    """Сериализатор навыков."""

    class Meta:
        model = Skill
        fields = ("id", "name")
