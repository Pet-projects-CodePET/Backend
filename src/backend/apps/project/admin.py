from django.contrib import admin

from .constants import PROJECTS_PER_PAGE
from .models import (
    Project,
    ProjectSpecialist,
    Skill,
    Specialist,
    Specialization,
)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ("name", "specialization")
    list_filter = ("specialization",)
    search_fields = ("name", "specialization__name")


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "creator",
        "started",
        "ended",
        "contacts",
        "busyness",
        "recruitment_status",
        "status",
        "direction",
    )
    list_filter = ("busyness", "status")
    search_fields = ("name", "description", "purpose", "creator__username")
    list_per_page = PROJECTS_PER_PAGE


@admin.register(ProjectSpecialist)
class ProjectSpecialistAdmin(admin.ModelAdmin):
    list_display = (
        "project",
        "specialist",
        "level",
        "count",
        "is_required",
    )
    list_filter = ("project",)
    search_fields = ("project",)
