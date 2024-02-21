# Generated by Django 5.0.1 on 2024-02-16 11:21

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Section",
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
                    "title",
                    models.TextField(max_length=100, verbose_name="Заголовок"),
                ),
                (
                    "description",
                    models.TextField(max_length=250, verbose_name="Текст"),
                ),
            ],
        ),
    ]
