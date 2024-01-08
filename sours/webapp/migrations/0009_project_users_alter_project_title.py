# Generated by Django 5.0 on 2024-01-05 08:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_issue_summary_project_title'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(related_name='projects_with_users', to=settings.AUTH_USER_MODEL, verbose_name='Пользователи'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='projects_with_title', to=settings.AUTH_USER_MODEL, verbose_name='Название'),
        ),
    ]
