from django.db import models


class CreatedModifiedFields(models.Model):
    """Базовая модель."""

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
