from rest_framework import serializers

from apps.project.models import (
    Project,
    ProjectSpecialist,
    Skill,
    Specialist,
    Specialization,
    Status,
)


class SpecialistSerializer(serializers.ModelSerializer):
    """Сериализатор получения специалистов."""

    class Meta:
        model = Specialist
        fields = ("id", "name", "specialization")


class SpecializationSerializer(serializers.ModelSerializer):
    """Сериализатор получения специализации."""

    class Meta:
        model = Specialization
        fields = ("id", "name")


class SkillSerializer(serializers.ModelSerializer):
    """Сериализатор получения навыков."""

    class Meta:
        model = Skill
        fields = ("id", "name")


class CustomSpecializationSerializer(SpecialistSerializer):
    specialization = SpecializationSerializer()

    class Meta:
        model = ProjectSpecialist
        fields = ("id", "specialization")


class StatusSerializer(serializers.ModelSerializer):
    """Сериализатор получения статуса проектов."""

    class Meta:
        model = Status
        fields = ("id", "name")


class ProjectSerializer(serializers.ModelSerializer):
    """Сериализатор получения проектов."""

    specialists = CustomSpecializationSerializer(many=True)

    status = StatusSerializer()
    skills = SkillSerializer(many=True)

    direction = serializers.SerializerMethodField()

    def get_direction(self, obj) -> str:
        return obj.get_direction_display()

    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "description",
            "started",
            "ended",
            "specialists",
            "skills",
            "direction",
            "status",
        )


class PreviewProjectSerializer(serializers.ModelSerializer):
    """Сериализатор получения превью проектов."""

    specialists = SpecialistSerializer(many=True)
    direction = serializers.SerializerMethodField()

    def get_direction(self, obj) -> str:
        return obj.get_direction_display()

    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "started",
            "ended",
            "specialists",
            "direction",
        )
