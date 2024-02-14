from rest_framework import generics
from rest_framework.response import Response

from apps.project.models import Project
from apps.users.models import User

from .models import Section
from .serializers import SectionSerializer


class SectionAPIList(generics.RetrieveAPIView, generics.ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class CounterApiView(generics.RetrieveAPIView):
    """Создала счетчик проектов и пользователей"""

    def get(self, request):
        count_project = Project.objects.count()
        count_user = User.objects.count()
        return Response({"projects": count_project, "users": count_user})
