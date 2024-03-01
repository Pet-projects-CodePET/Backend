from datetime import date

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from apps.general.models import Skill, Specialization
from apps.profile.constants import (
    BOOL_CHOICES,
    LEVEL_CHOICES,
    MAX_LEN_NICKNAME,
)
from apps.profile.validators import (
    validate_about,
    validate_image,
    validate_nickname,
    validate_phone_number,
    validate_portfolio,
)
from apps.users.models import User


class UserSkill(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)


class UserSpecialization(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    specialization_id = models.ForeignKey(
        Specialization, on_delete=models.CASCADE
    )


class Profile(models.Model):
    avatar = models.ImageField(
        verbose_name="Аватар", upload_to="images/", validators=[validate_image]
    )
    nickname = models.CharField(
        verbose_name="Никнейм",
        max_length=MAX_LEN_NICKNAME,
        blank=False,
        unique=True,
        validators=[validate_nickname],
    )
    name = models.CharField(
        verbose_name="Имя",
        max_length=MAX_LEN_NICKNAME,
        blank=False,
        validators=[validate_nickname],
    )
    about = models.TextField(
        verbose_name="О себе", blank=False, validators=[validate_about]
    )
    portfolio_link = models.URLField(
        blank=False, validators=[validate_portfolio]
    )
    contacts = models.TextField(
        blank=False, validators=[validate_phone_number]
    )
    birthday = models.DateField(
        verbose_name="Дата рождения",
        blank=False,
        null=False,
        validators=[
            MinValueValidator(limit_value=date(1950, 1, 1)),
            MaxValueValidator(limit_value=date.today()),
        ],
    )
    country = models.CharField(verbose_name="Страна", max_length=255)
    city = models.CharField(verbose_name="Город", max_length=255)
    specialization = models.ForeignKey(
        UserSpecialization,
        verbose_name="Специальность",
        null=False,
        on_delete=models.CASCADE,
    )
    skill = models.ForeignKey(
        UserSkill, verbose_name="Навыки", null=False, on_delete=models.CASCADE
    )
    level = models.CharField(
        verbose_name="Уровень квалификации",
        max_length=255,
        choices=LEVEL_CHOICES,
    )
    ready_to_participate = models.BooleanField(
        verbose_name="Готовность к участию в проектах", choices=BOOL_CHOICES
    )
