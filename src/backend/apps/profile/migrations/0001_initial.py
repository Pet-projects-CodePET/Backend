# Generated by Django 5.0.1 on 2024-03-07 16:29

import apps.profile.validators
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("general", "0002_section_page_id"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserSkill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "skill",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="general.skill",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserSpecialization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "specialization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="general.specialization",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        upload_to="images/",
                        validators=[apps.profile.validators.validate_image],
                        verbose_name="Аватар",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=30,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Введите кириллицу или латиницу",
                                regex="^[a-zA-Zа-яА-Я -]+$",
                            )
                        ],
                        verbose_name="Имя",
                    ),
                ),
                (
                    "about",
                    models.TextField(
                        max_length=750,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Введите кириллицу или латиницу",
                                regex="^[a-zA-Zа-яА-Я0-9\\s!@#$%^&*()-_+=<>?]+$",
                            )
                        ],
                        verbose_name="О себе",
                    ),
                ),
                (
                    "portfolio_link",
                    models.URLField(
                        max_length=256,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Добавьте ссылку на любую платформу, где размещено ваше портфолио",
                                regex="^(?i)(http|https):\\/\\/(?=.*[a-zA-Z])(?=.*\\d)(?=.*[!@#$%^&*()_+])[a-zA-Z\\d!@#$%^&*()_+]+(?:\\.[a-zA-Z\\d!@#$%^&*()_+]+)*(?:\\/[a-zA-Z\\d!@#$%^&*()_+]+)*(?:\\/[a-zA-Z\\d!@#$%^&*()_+]+)*(?:#[a-zA-Z\\d!@#$%^&*()_+]*)?$",
                            )
                        ],
                    ),
                ),
                (
                    "phone_number",
                    models.TextField(
                        max_length=12,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Телефон может содержать: цифры, спецсимволы, длина не должна превышать 12 символов",
                                regex="^\\+7\\(\\d{3}\\)\\d{3}-\\d{2}-\\d{2}$",
                            )
                        ],
                        verbose_name="Номер телефона",
                    ),
                ),
                (
                    "telegram",
                    models.CharField(
                        max_length=32,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Некорректный формат введенных данных",
                                regex="^[a-zA-Z0-9_]+$",
                            )
                        ],
                        verbose_name="Ник в телеграме",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=256,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Некорректный формат введенных данных",
                                regex="^^(?![-._])[a-zA-Z0-9.-_](?![-._])[a-zA-Z0-9._%+-]{0,63}@(?![.-])[a-zA-Z0-9.-](?<![-.])\\.[a-zA-Z]{2,63}(?<![-.])$",
                            )
                        ],
                        verbose_name="E-mail",
                    ),
                ),
                (
                    "birthday",
                    models.DateField(
                        validators=[apps.profile.validators.AgeValidator],
                        verbose_name="Дата рождения",
                    ),
                ),
                (
                    "country",
                    models.CharField(max_length=255, verbose_name="Страна"),
                ),
                (
                    "city",
                    models.CharField(max_length=255, verbose_name="Город"),
                ),
                (
                    "level",
                    models.IntegerField(
                        choices=[
                            (1, "intern"),
                            (2, "junior"),
                            (3, "middle"),
                            (4, "senior"),
                            (5, "lead"),
                        ],
                        verbose_name="Уровень квалификации",
                    ),
                ),
                (
                    "ready_to_participate",
                    models.BooleanField(
                        choices=[(True, "Готов"), (False, "Не готов")],
                        verbose_name="Готовность к участию в проектах",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
                (
                    "skill",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="profile.userskill",
                        verbose_name="Навыки",
                    ),
                ),
                (
                    "specialization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="profile.userspecialization",
                        verbose_name="Специальность",
                    ),
                ),
            ],
        ),
    ]
