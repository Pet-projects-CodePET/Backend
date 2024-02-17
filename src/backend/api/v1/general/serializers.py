from rest_framework import serializers
from src.backend.apps.general.models import Section


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = "__all__"
