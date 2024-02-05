from django.contrib import admin

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
        "duration",
        "level",
        "busyness",
        "status",
    )
    list_filter = ("level", "busyness", "status")
    search_fields = ("name", "description", "purpose", "creator__username")
    readonly_fields = ("duration",)
    list_per_page = 10

    def duration(self, instance):
        return instance.duration

    duration.short_description = "Продолжительность в месяцах"
