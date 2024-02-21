# Generated by Django 5.0.1 on 2024-02-21 12:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0006_userfavoriteprojectsrelation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userfavoriteprojectsrelation",
            name="projects",
            field=models.ManyToManyField(
                related_name="favorited_by",
                to="project.project",
                verbose_name="Избранные проекты пользователя",
            ),
        ),
    ]
