# Generated by Django 5.0.1 on 2024-02-12 13:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0004_alter_project_busyness"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="specialization",
            options={
                "verbose_name": "Специализация",
                "verbose_name_plural": "Специализации",
            },
        ),
        migrations.RemoveField(
            model_name="specialization",
            name="quantity",
        ),
        migrations.AddField(
            model_name="project",
            name="contacts",
            field=models.TextField(
                default="", max_length=256, verbose_name="Контакты для связи"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="project",
            name="direction",
            field=models.IntegerField(
                choices=[(1, "Десктоп"), (2, "Веб"), (3, "Мобильная")],
                default=1,
                verbose_name="Направление разработки",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="project",
            name="participants",
            field=models.ManyToManyField(
                related_name="project_participants",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Команда проекта",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="busyness",
            field=models.IntegerField(
                choices=[(1, "10"), (2, "20"), (3, "30"), (4, "40")],
                verbose_name="Занятость в часах в неделю",
            ),
        ),
    ]
