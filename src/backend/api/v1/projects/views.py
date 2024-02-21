from rest_framework import generics
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.project.models import Project, UserFavoriteProjectsRelation
from api.v1.projects.serializers import ProjectsSerializer


class AddFavoriteProject(generics.CreateAPIView):
    serializer_class = ProjectsSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def perform_create(self, serializer):
        user = self.request.user
        project_name = serializer.validated_data["name"]

        try:
            project = Project.objects.get(name=project_name)
        except Project.DoesNotExist:
            raise NotFound(f'Project with name "{project_name}" not found.')

        if UserFavoriteProjectsRelation.objects.filter(
            user=user, projects=project
        ).exists():
            raise PermissionDenied(
                f'Project "{project_name}" is already a favorite.'
            )

        user.favorite_projects.add(project)


class UserFavoriteProjectsListAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(favorited_by__user=user)
