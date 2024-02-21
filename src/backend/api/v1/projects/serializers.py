from rest_framework.serializers import ModelSerializer

from apps.project.models import Project


class ProjectsSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
