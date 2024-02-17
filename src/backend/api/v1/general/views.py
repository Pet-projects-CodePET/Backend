from django.db import connection
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics
from rest_framework.response import Response
from src.backend.api.v1.general.serializers import SectionSerializer
from src.backend.apps.general.models import Section


class SectionAPIList(generics.RetrieveAPIView, generics.ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class CounterApiView(generics.RetrieveAPIView):
    """Создала счетчик проектов и пользователей"""

    @method_decorator(cache_page(600))
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT count(*) from project_project union all SELECT count(*) from users_user "
            )
            row = cursor.fetchall()
        return Response({"projects": row[0][0], "users": row[1][0]})
