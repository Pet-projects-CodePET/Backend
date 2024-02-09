from rest_framework import generics

from .models import Section
from .serializers import SectionSerializer


class SectionAPIList(generics.RetrieveAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
