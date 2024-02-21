from rest_framework import serializers

from apps.general.models import Section, Skill, Specialization


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"


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
