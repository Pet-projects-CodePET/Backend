from django.db import models

from apps.general.constants import (
    MAX_LENGTH_SKILL_NAME,
    MAX_LENGTH_SPECIALIZATION_NAME,
)


class CreatedModifiedFields(models.Model):
    """Базовая модель."""

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Skill(models.Model):
    """Модель навыков."""

    name = models.CharField(
        verbose_name="Название",
        max_length=MAX_LENGTH_SKILL_NAME,
    )

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self) -> str:
        return self.name


class Specialization(models.Model):
    """Модель специальности."""

    name = models.CharField(
        verbose_name="Название",
        max_length=MAX_LENGTH_SPECIALIZATION_NAME,
    )

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"

    def __str__(self) -> str:
        return self.name
