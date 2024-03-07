from django.core.validators import RegexValidator
from django.db import models

from apps.general.constants import LEVEL_CHOICES
from apps.general.models import Skill, Specialization
from apps.profile.constants import (
    BOOL_CHOICES,
    MAX_LENGTH_ABOUT,
    MAX_LENGTH_CITY,
    MAX_LENGTH_COUNTRY,
    MAX_LENGTH_EMAIL,
    MAX_LENGTH_NAME,
    MAX_LENGTH_PHONE_NUMBER,
    MAX_LENGTH_TELEGRAM,
    MAX_LENGTH_URL,
    MIN_LENGTH_ABOUT,
    MIN_LENGTH_EMAIL,
    MIN_LENGTH_NAME,
    MIN_LENGTH_PORTFOLIO,
    MIN_LENGTH_TELEGRAM,
)
from apps.profile.validators import (
    AgeValidator,
    MinLengthValidator,
    validate_image,
)
from apps.users.models import User


class UserSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)


class UserSpecialization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialization = models.ForeignKey(
        Specialization, on_delete=models.CASCADE
    )


class Profile(models.Model):
    avatar = models.ImageField(
        verbose_name="Аватар", upload_to="images/", validators=[validate_image]
    )
    name = models.CharField(
        verbose_name="Имя",
        max_length=MAX_LENGTH_NAME,
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Zа-яА-Я -]+$",
                message="Введите кириллицу или латиницу",
            )
        ],
        blank=False,
    )
    about = models.TextField(
        verbose_name="О себе",
        blank=False,
        max_length=MAX_LENGTH_ABOUT,
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Zа-яА-Я0-9\s!@#$%^&*()-_+=<>?]+$",
                message="Введите кириллицу или латиницу",
            )
        ],
    )
    portfolio_link = models.URLField(
        unique=True,
        blank=False,
        max_length=MAX_LENGTH_URL,
        validators=[
            RegexValidator(
                regex=r"^(?i)(http|https):\/\/(?=.*[a-zA-Z])(?=.*\d)(?=.*[!@#$%^&*()_+])[a-zA-Z\d!@#$%^&*()_+]+(?:\.[a-zA-Z\d!@#$%^&*()_+]+)*(?:\/[a-zA-Z\d!@#$%^&*()_+]+)*(?:\/[a-zA-Z\d!@#$%^&*()_+]+)*(?:#[a-zA-Z\d!@#$%^&*()_+]*)?$",
                message="Добавьте ссылку на любую платформу, где размещено ваше портфолио",
            )
        ],
    )
    phone_number = models.TextField(
        max_length=MAX_LENGTH_PHONE_NUMBER,
        verbose_name="Номер телефона",
        validators=[
            RegexValidator(
                regex=r"^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$",
                message="Телефон может содержать: цифры, спецсимволы, длина не должна превышать 12 символов",
            )
        ],
    )
    telegram = models.CharField(
        max_length=MAX_LENGTH_TELEGRAM,
        verbose_name="Ник в телеграме",
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z0-9_]+$",
                message="Некорректный формат введенных данных",
            )
        ],
    )
    email = models.EmailField(
        verbose_name="E-mail",
        max_length=MAX_LENGTH_EMAIL,
        validators=[
            RegexValidator(
                regex=r"^^(?![-._])[a-zA-Z0-9.-_](?![-._])[a-zA-Z0-9._%+-]{0,63}@(?![.-])[a-zA-Z0-9.-](?<![-.])\.[a-zA-Z]{2,63}(?<![-.])$",
                message="Некорректный формат введенных данных",
            )
        ],
    )
    birthday = models.DateField(
        verbose_name="Дата рождения",
        blank=False,
        null=False,
        validators=[AgeValidator],
    )
    country = models.CharField(
        verbose_name="Страна", max_length=MAX_LENGTH_COUNTRY
    )
    city = models.CharField(verbose_name="Город", max_length=MAX_LENGTH_CITY)
    specialization = models.ForeignKey(
        UserSpecialization,
        verbose_name="Специальность",
        null=False,
        on_delete=models.CASCADE,
    )
    skill = models.ForeignKey(
        UserSkill, verbose_name="Навыки", null=False, on_delete=models.CASCADE
    )
    level = models.IntegerField(
        verbose_name="Уровень квалификации",
        choices=LEVEL_CHOICES,
    )
    ready_to_participate = models.BooleanField(
        verbose_name="Готовность к участию в проектах", choices=BOOL_CHOICES
    )
    user = models.ForeignKey(
        User, verbose_name="Пользователь", on_delete=models.CASCADE
    )

    def clean(self):
        super().clean()

        validator_name = MinLengthValidator(min_length=MIN_LENGTH_NAME)
        validator_name.validate(self.name)

        validator_about = MinLengthValidator(min_length=MIN_LENGTH_ABOUT)
        validator_about.validate(self.about)

        validator_portfolio = MinLengthValidator(
            min_length=MIN_LENGTH_PORTFOLIO
        )
        validator_portfolio.validate(self.portfolio_link)

        validator_telegram = MinLengthValidator(min_length=MIN_LENGTH_TELEGRAM)
        validator_telegram.validate(self.telegram)

        validator_email = MinLengthValidator(min_length=MIN_LENGTH_EMAIL)
        validator_email.validate(self.email)
