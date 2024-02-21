from django.contrib.auth import get_user_model
from django.db import models

from apps.general.models import CreatedModifiedFields

from .constants import (
    BUSYNESS_CHOICES,
    CONTACTS_LENGTH,
    DESCRIPTION_LENGTH,
    DIRECTION_CHOICES,
    NAME_LENGTH,
    STATUS_CHOICES,
)

User = get_user_model()


class Specialization(models.Model):
    """
    Модель представляющая специализацию, подразделяется на специальности.
    """

    name = models.CharField("Название", max_length=NAME_LENGTH)

    class Meta:
        verbose_name = "Специализация"
        verbose_name_plural = "Специализации"

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
        choices=BUSYNESS_CHOICES,
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
    contacts = models.TextField(
        "Контакты для связи", max_length=CONTACTS_LENGTH
    )
    direction = models.IntegerField(
        choices=DIRECTION_CHOICES,
        verbose_name="Направление разработки",
    )
    participants = models.ManyToManyField(
        User,
        related_name="project_participants",
        verbose_name="Команда проекта",
    )

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ("-created",)

    def __str__(self) -> str:
        return self.name


class UserFavoriteProjectsRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    projects = models.ManyToManyField(
        Project,
        verbose_name="Избранные проекты пользователя",
        related_name="favorited_by"
    )

    class Meta:
        verbose_name = "Отношение пользователя к его избранным книгам"
        verbose_name_plural = "Отношения пользователей к их избранным книгам"
        ordering = ("user",)

    def __str__(self):
        return self.user.name
