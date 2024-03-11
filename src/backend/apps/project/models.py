from django.contrib.auth import get_user_model
from django.db import models

from apps.general.constants import LEVEL_CHOICES
from apps.general.models import CreatedModifiedFields, Skill, Specialization

from .constants import (
    BUSYNESS_CHOICES,
    DIRECTION_CHOICES,
    MAX_LENGTH_CONTACTS,
    MAX_LENGTH_DESCRIPTION,
    MAX_LENGTH_PROFESSION_NAME,
    MAX_LENGTH_PROJECT_NAME,
    MAX_LENGTH_PURPOSE,
    STATUS_CHOICES,
)

User = get_user_model()


class Specialist(models.Model):
    """Модель специалиста."""

    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.CASCADE,
        related_name="specialists",
        verbose_name="Специальность",
    )
    name = models.CharField(
        verbose_name="Название специализации",
        max_length=MAX_LENGTH_PROFESSION_NAME,
    )

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"

    def __str__(self) -> str:
        return f"{self.specialization.name} {self.name}"


class Project(CreatedModifiedFields):
    """Модель проект."""

    name = models.CharField(
        verbose_name="Название проекта",
        max_length=MAX_LENGTH_PROJECT_NAME,
    )
    description = models.TextField(
        verbose_name="Описание проекта",
        max_length=MAX_LENGTH_DESCRIPTION,
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="created_projects",
        verbose_name="Организатор",
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="owned_projects",
        verbose_name="Владелец",
    )
    started = models.DateField(
        verbose_name="Начало проекта",
        null=True,
        blank=True,
    )
    ended = models.DateField(
        verbose_name="Окончание проекта",
        null=True,
        blank=True,
    )
    busyness = models.PositiveSmallIntegerField(
        verbose_name="Занятость в часах в неделю",
        choices=BUSYNESS_CHOICES,
    )
    recruitment_status = models.BooleanField(
        verbose_name="Статус набора участников",
        default=False,
    )
    status = models.PositiveSmallIntegerField(
        verbose_name="Статус проекта",
        choices=STATUS_CHOICES,
    )
    contacts = models.TextField(
        verbose_name="Контакты для связи",
        max_length=MAX_LENGTH_CONTACTS,
    )
    direction = models.PositiveSmallIntegerField(
        verbose_name="Направление разработки",
        choices=DIRECTION_CHOICES,
    )
    participants = models.ManyToManyField(
        User,
        verbose_name="Участники проекта",
        related_name="projects_participated",
        blank=True,
    )
    skills = models.ManyToManyField(
        Skill, related_name="projects", verbose_name="Проекты"
    )
    level = models.PositiveSmallIntegerField(
        verbose_name="Уровень", choices=LEVEL_CHOICES, null=True, blank=True
    )

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ("-created",)

    def __str__(self) -> str:
        return self.name


class ProjectSpecialist(models.Model):
    """Модель количества специалистов необходимых проекту."""

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        verbose_name="Проект",
    )
    specialist = models.ForeignKey(
        Specialist,
        on_delete=models.CASCADE,
        verbose_name="Специалист",
    )
    skills = models.ManyToManyField(
        Skill,
        verbose_name="Навыки",
    )
    count = models.PositiveSmallIntegerField(
        verbose_name="Количество",
    )
    level = models.PositiveSmallIntegerField(
        verbose_name="Уровень",
        choices=LEVEL_CHOICES,
    )
    is_required = models.BooleanField(
        verbose_name="Требуется для проекта",
        default=False,
    )

    class Meta:
        verbose_name = "Специалист проекта"
        verbose_name_plural = "Специалисты проекта"
        default_related_name = "project_specialists"
