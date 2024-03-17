from rest_framework import serializers

from apps.general.models import Section, Skill, Specialist


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"


class SpecialistSerializer(serializers.ModelSerializer):
    """Сериализатор специализации."""

    class Meta:
        model = Specialist
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    """Сериализатор навыков."""

    class Meta:
        model = Skill
        fields = "__all__"
