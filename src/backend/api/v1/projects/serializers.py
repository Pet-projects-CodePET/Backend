from rest_framework import serializers

from api.v1.general.serializers import (
    SkillSerializer,
    SpecializationSerializer,
)
from apps.project.models import (
    Project,
    ProjectSpecialist,
    Specialist,
    Specialization,
)


class SpecialistSerializer(serializers.ModelSerializer):
    """Сериализатор специалистов."""

    specialization = SpecializationSerializer()

    class Meta:
        model = Specialist
        fields = (
            "id",
            "name",
            "specialization",
        )


class ProjectSpecialistSerializer(SpecialistSerializer):
    """Сериализатор специалистов необходимых проекту."""

    specialist = SpecialistSerializer()
    skills = SkillSerializer(many=True)
    level = serializers.SerializerMethodField()

    class Meta:
        model = ProjectSpecialist
        fields = (
            "specialist",
            "skills",
            "count",
            "level",
            "is_required",
        )

    def get_level(self, obj) -> str:
        return obj.get_level_display()


class ProjectSerializer(serializers.ModelSerializer):
    """Сериализатор проектов."""

    project_specialists = ProjectSpecialistSerializer(many=True)
    direction = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    def get_direction(self, obj) -> str:
        return obj.get_direction_display()

    def get_status(self, obj) -> str:
        return obj.get_status_display()

    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "description",
            "started",
            "ended",
            "direction",
            "creator",
            "owner",
            "project_specialists",
            "status",
        )


class ProjectPreviewMainSerializer(serializers.ModelSerializer):
    """Сериализатор превью проектов."""

    specializations = serializers.SerializerMethodField()
    direction = serializers.SerializerMethodField()

    def get_direction(self, obj) -> str:
        return obj.get_direction_display()

    def get_specializations(self, obj) -> list[str]:
        return [
            specialist.specialist.specialization.name
            for specialist in obj.project_specialists.all()
        ]

    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "started",
            "ended",
            "direction",
            "specializations",
        )
