# Generated by Django 5.2.2 on 2025-06-08 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_project_featuted"),
    ]

    operations = [
        migrations.RenameField(
            model_name="project",
            old_name="featuted",
            new_name="featured",
        ),
    ]
