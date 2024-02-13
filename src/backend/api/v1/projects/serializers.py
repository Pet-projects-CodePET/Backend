from rest_framework import serializers

from apps.project.models import Project, Skill, Specialist, Status


class SpecialistSerializer(serializers.ModelSerializer):
    """Сериализатор получения специалистов."""

    class Meta:
        model = Specialist
        fields = ("id", "name")


class SkillSerializer(serializers.ModelSerializer):
    """Сериализатор получения навыков."""

    class Meta:
        model = Skill
        fields = ("id", "name")


class StatusSerializer(serializers.ModelSerializer):
    """Сериализатор получения статуса проектов."""

    class Meta:
        model = Status
        fields = ("id", "name")


class ProjectSerializer(serializers.ModelSerializer):
    """Сериализатор получения проектов."""

    specialists = SpecialistSerializer(many=True)

    status = StatusSerializer()
    skills = SkillSerializer(many=True)

    direction = serializers.SerializerMethodField()

    def get_direction(self, obj):
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
            "status",
            "direction",
        )
