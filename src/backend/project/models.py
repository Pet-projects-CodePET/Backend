from django.contrib.auth import get_user_model
from django.db import models

from apps.general.models import CreatedModifiedFields

from .constants import (
    BUSYNESS_CHOICES,
    BUSYNESS_LENGTH,
    DAYS_IN_MONTH,
    DESCRIPTION_LENGTH,
    NAME_LENGTH,
)

User = get_user_model()


class Specialization(models.Model):
    name = models.CharField("Название", max_length=NAME_LENGTH)
    quantity = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

    def __str__(self) -> str:
        return self.name


class Specialist(models.Model):
    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.CASCADE,
        related_name="specialists",
        verbose_name="Специализация",
    )
    name = models.CharField("Название", max_length=NAME_LENGTH)

    class Meta:
        verbose_name = "Специалист"
        verbose_name_plural = "Специалисты"

    def __str__(self) -> str:
        return self.name


class Level(models.Model):
    name = models.CharField("Название", max_length=NAME_LENGTH)

    class Meta:
        verbose_name = "Уровень"
        verbose_name_plural = "Уровни"

    def __str__(self) -> str:
        return self.name


class Status(models.Model):
    name = models.CharField("Название", max_length=NAME_LENGTH)

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    name = models.CharField("Название", max_length=NAME_LENGTH)

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self) -> str:
        return self.name


class Project(CreatedModifiedFields):
    name = models.CharField("Название проекта", max_length=NAME_LENGTH)
    description = models.TextField(
        "Описание проекта", max_length=DESCRIPTION_LENGTH
    )
    purpose = models.CharField("Цель проекта", max_length=NAME_LENGTH)
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="projects",
        verbose_name="Организатор",
    )
    started = models.DateField("Дата начала проекта", null=True, blank=True)
    ended = models.DateField("Дата окончания проекта", null=True, blank=True)
    specialists = models.ManyToManyField(
        Specialist,
        related_name="projects",
        verbose_name="Специалисты",
    )
    level = models.ForeignKey(
        Level,
        on_delete=models.CASCADE,
        verbose_name="Уровень",
    )
    skills = models.ManyToManyField(
        Skill,
        related_name="projects",
        verbose_name="Навыки",
    )
    busyness = models.CharField(
        max_length=BUSYNESS_LENGTH,
        choices=BUSYNESS_CHOICES,
        verbose_name="Занятость",
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        verbose_name="Статус",
    )

    @property
    def duration(self):
        if self.ended is not None and self.started is not None:
            duration = self.ended - self.started
            months = duration.days // DAYS_IN_MONTH
            return months
        return None

    duration.fget.short_description = "Продолжительность"

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ("-created",)

    def __str__(self) -> str:
        return self.name
