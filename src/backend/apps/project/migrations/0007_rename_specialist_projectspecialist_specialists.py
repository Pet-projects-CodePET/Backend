# Generated by Django 5.0.1 on 2024-02-16 08:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "project",
            "0006_alter_specialist_options_remove_project_level_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="projectspecialist",
            old_name="specialist",
            new_name="specialists",
        ),
    ]
