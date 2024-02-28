from django.db import connection
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.response import Response

from apps.general.models import Section

from .serializers import SectionSerializer


class SectionViewSet(viewsets.ModelViewSet):
    """Текстовая секция на странице"""

    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["page_id"]


class CounterApiView(generics.RetrieveAPIView):
    """Счетчик проектов и пользователей"""

    @method_decorator(cache_page(600))
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT count(*) from project_project union all SELECT count(*) from users_user "
            )
            row = cursor.fetchall()
        return Response({"projects": row[0][0], "users": row[1][0]})
