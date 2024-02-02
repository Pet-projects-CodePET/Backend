from django.db import models

# from apps.content_pages.utilities import path_by_app_and_class_name


class CreatedModifiedFields(models.Model):
    """Базовая модель"""

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
