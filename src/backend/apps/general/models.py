from django.db import models


class CreatedModifiedFields(models.Model):
    """
    Абстрактная модель. Поля времени создания и последней модификации объекта.
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
