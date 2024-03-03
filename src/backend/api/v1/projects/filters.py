from django_filters.rest_framework import FilterSet
from django_filters import filters

from apps.general.constants import LEVEL_CHOICES
from apps.general.models import Skill
from apps.project.constants import BUSYNESS_CHOICES, STATUS_CHOICES, DIRECTION_CHOICES
from apps.project.models import Project


class ProjectFilter(FilterSet):
    """
    Класс для фильтрации проектов по имени, дате начала, дате конца, занятости в часах в неделю, статусу набора
    участников, статусу проекта, направлению разработки, навыкам и уровню
    """
    name = filters.CharFilter(lookup_expr="icontains")
    started = filters.DateFromToRangeFilter()
    ended = filters.DateFromToRangeFilter()
    busyness = filters.MultipleChoiceFilter(choices=BUSYNESS_CHOICES)
    recruitment_status = filters.BooleanFilter()
    status = filters.MultipleChoiceFilter(choices=STATUS_CHOICES)
    direction = filters.MultipleChoiceFilter(choices=DIRECTION_CHOICES)
    skill = filters.ModelMultipleChoiceFilter(queryset=Skill.objects.all())
    level = filters.MultipleChoiceFilter(choices=LEVEL_CHOICES)

    class Meta:
        model = Project
        fields = (
            "name", "started", "ended", "busyness", "recruitment_status", "status", "direction", "skill", "level"
        )
