from django.db import models

from .constants import DESCRIPRION_LENGTH, TITLE_LENGTH


class CreatedModifiedFields(models.Model):
    """
    Абстрактная модель. Поля времени создания и последней модификации объекта.
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Section(models.Model):
    """Секции на главной странице"""

    title = models.TextField(
        verbose_name="Заголовок", max_length=TITLE_LENGTH, null=False
    )
    description = models.TextField(
        verbose_name="Текст", max_length=DESCRIPRION_LENGTH, null=False
    )
    page_id = models.IntegerField(
        verbose_name="Идентификатор страницы", null=False, default=0
    )

    def __str__(self):
        return self.title
