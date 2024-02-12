from django.contrib import admin

from .constants import LIST_PER_PAGE
from .models import Level, Project, Skill, Specialist, Specialization, Status


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
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
        "creator",
        "started",
        "ended",
        "contacts",
        "level",
        "busyness",
        "recruitment_status",
        "status",
        "direction",
    )
    list_filter = ("level", "busyness", "status")
    search_fields = ("name", "description", "purpose", "creator__username")
    list_per_page = LIST_PER_PAGE
