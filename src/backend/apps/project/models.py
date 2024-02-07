from django.contrib.auth import get_user_model
from django.db import models

from apps.general.models import CreatedModifiedFields

from .constants import DESCRIPTION_LENGTH, NAME_LENGTH, STATUS_CHOICES

User = get_user_model()


class Specialization(models.Model):
    """
    Модель представляющая специализацию, подразделяется на специальности.
    """

    name = models.CharField("Название", max_length=NAME_LENGTH)
    quantity = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

    def __str__(self) -> str:
        return self.name


class Specialist(models.Model):
    """
    Модель представляющая специальность(специалиста), входящую в специализацию.
    """

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
    """
    Модель представляющая уровень участников.
    """

    name = models.CharField("Название", max_length=NAME_LENGTH)

    class Meta:
        verbose_name = "Уровень"
        verbose_name_plural = "Уровни"

    def __str__(self) -> str:
        return self.name


class Status(models.Model):
    """
    Модель представляющая статус проекта.
    """

    name = models.CharField("Название", max_length=NAME_LENGTH)

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    """
    Модель представляющая необходимые для проекта навыки.
    """

    name = models.CharField("Название", max_length=NAME_LENGTH)

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self) -> str:
        return self.name


class Project(CreatedModifiedFields):
    """
    Модель представляющая проект.
    """

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
    busyness = models.IntegerField(
        verbose_name="Занятость в часах в неделю",
    )
    recruitment_status = models.IntegerField(
        choices=STATUS_CHOICES,
        verbose_name="Статус набора участников",
        default=1,
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        verbose_name="Статус проекта",
    )

    @property
    def duration(self):
        """
        Вычисляет и возвращает продолжительность проекта в днях.
        """
        if self.ended is not None and self.started is not None:
            duration = self.ended - self.started
            return duration.days
        return None

    duration.fget.short_description = "Продолжительность"

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ("-created",)

    def __str__(self) -> str:
        return self.name
