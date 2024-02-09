from django.db import models


class CreatedModifiedFields(models.Model):
    """Базовая модель."""

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Section(models.Model):
    """Секции на главной странице"""

    title = models.TextField(
        verbose_name="Заголовок", max_length=55, null=False
    )
    description = models.TextField(
        verbose_name="Текст", max_length=160, null=False
    )

    def __str__(self):
        return self.title
