from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

from apps.general.constants import LEVEL_CHOICES
from apps.general.models import (
    ContactsFields,
    CreatedModifiedFields,
    Skill,
    Specialist,
)
from apps.projects.constants import (
    BUSYNESS_CHOICES,
    LENGTH_DESCRIPTION_ERROR_TEXT,
    LENGTH_DIRECTION_NAME_ERROR_TEXT,
    LENGTH_LINK_ERROR_TEXT,
    LENGTH_PROJECT_NAME_ERROR_TEXT,
    MAX_LENGTH_DESCRIPTION,
    MAX_LENGTH_DIRECTION_NAME,
    MAX_LENGTH_LINK,
    MAX_LENGTH_PROJECT_NAME,
    MIN_LENGTH_DESCRIPTION,
    MIN_LENGTH_DIRECTION_NAME,
    MIN_LENGTH_LINK,
    MIN_LENGTH_PROJECT_NAME,
    REGEX_DIRECTION_NAME,
    REGEX_DIRECTION_NAME_ERROR_TEXT,
    REGEX_PROJECT_NAME,
    REGEX_PROJECT_NAME_ERROR_TEXT,
    STATUS_CHOICES,
)

User = get_user_model()


class Direction(models.Model):
    """Модель направления разработки."""

    name = models.CharField(
        verbose_name="Название",
        max_length=MAX_LENGTH_DIRECTION_NAME,
        unique=True,
        validators=(
            MinLengthValidator(
                limit_value=MIN_LENGTH_DIRECTION_NAME,
                message=LENGTH_DIRECTION_NAME_ERROR_TEXT,
            ),
            RegexValidator(
                regex=REGEX_DIRECTION_NAME,
                message=REGEX_DIRECTION_NAME_ERROR_TEXT,
            ),
        ),
    )

    class Meta:
        verbose_name = "Направление разработки"
        verbose_name_plural = "Направления разработки"

    def __str__(self) -> str:
        """Метод строкового представления объекта направления разработки."""

        return self.name


class Project(CreatedModifiedFields, ContactsFields):
    """Модель проекта."""

    ACTIVE = 1
    ENDED = 2
    DRAFT = 3

    name = models.CharField(
        verbose_name="Название",
        max_length=MAX_LENGTH_PROJECT_NAME,
        validators=(
            MinLengthValidator(
                limit_value=MIN_LENGTH_PROJECT_NAME,
                message=LENGTH_PROJECT_NAME_ERROR_TEXT,
            ),
            RegexValidator(
                regex=REGEX_PROJECT_NAME,
                message=REGEX_PROJECT_NAME_ERROR_TEXT,
            ),
        ),
    )
    description = models.TextField(
        verbose_name="Описание",
        max_length=MAX_LENGTH_DESCRIPTION,
        blank=True,
        validators=(
            MinLengthValidator(
                limit_value=MIN_LENGTH_DESCRIPTION,
                message=LENGTH_DESCRIPTION_ERROR_TEXT,
            ),
        ),
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
        verbose_name="Дата начала",
        null=True,
        blank=True,
    )
    ended = models.DateField(
        verbose_name="Дата завершения",
        null=True,
        blank=True,
    )
    busyness = models.PositiveSmallIntegerField(
        verbose_name="Занятость (час/нед)",
        choices=BUSYNESS_CHOICES,
        null=True,
        blank=True,
    )
    status = models.PositiveSmallIntegerField(
        verbose_name="Статус",
        choices=STATUS_CHOICES,
    )
    directions = models.ManyToManyField(
        Direction,
        verbose_name="Направления разработки",
        related_name="projects_direction",
        blank=True,
    )
    link = models.URLField(
        verbose_name="Ссылка",
        max_length=MAX_LENGTH_LINK,
        validators=(
            MinLengthValidator(
                limit_value=MIN_LENGTH_LINK,
                message=LENGTH_LINK_ERROR_TEXT,
            ),
        ),
    )
    participants = models.ManyToManyField(
        User,
        verbose_name="Участники",
        related_name="projects_participated",
        blank=True,
    )

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ("-created",)
        constraints = (
            models.UniqueConstraint(
                fields=("creator", "name"),
                name=("%(app_label)s_%(class)s_unique_name_per_creator"),
            ),
        )

    def __str__(self) -> str:
        """Метод строкового представления объекта проекта."""

        return self.name


class ProjectSpecialist(models.Model):
    """Модель специалиста необходимого проекту."""

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
        verbose_name="Требуется",
        default=False,
    )

    class Meta:
        verbose_name = "Специалист проекта"
        verbose_name_plural = "Специалисты проекта"
        default_related_name = "project_specialists"
        constraints = (
            models.UniqueConstraint(
                fields=("project", "specialist", "level"),
                name="%(app_label)s_%(class)s_unique_specialist_per_project",
            ),
        )
