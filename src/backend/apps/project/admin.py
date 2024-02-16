from django.contrib import admin

from .constants import LIST_PER_PAGE
from .models import (
    Level,
    Project,
    ProjectSpecialist,
    Skill,
    Specialist,
    Specialization,
    Status,
)


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
        "description",
        "purpose",
        "creator",
        "started",
        "ended",
        "_specialists",
        "_skills",
        "contacts",
        "busyness",
        "recruitment_status",
        "status",
        "direction",
    )
    list_filter = ("busyness", "status")
    search_fields = ("name", "description", "purpose", "creator__username")
    list_per_page = LIST_PER_PAGE

    def _skills(self, obj):
        return ", ".join([skill.name for skill in obj.skills.all()])

    def _specialists(self, obj):
        specialists = ProjectSpecialist.objects.filter(project=obj)
        return "\n".join(
            [
                f"{specialist.specialists.name} (Level: {specialist.level}, Required: {specialist.is_required})"
                for specialist in specialists
            ]
        )


@admin.register(ProjectSpecialist)
class ProjectSpecialistAdmin(admin.ModelAdmin):
    list_display = (
        "project",
        "specialists",
        "specialists_count",
        "level",
        "is_required",
    )
    list_filter = ("project",)
    search_fields = ("project",)
