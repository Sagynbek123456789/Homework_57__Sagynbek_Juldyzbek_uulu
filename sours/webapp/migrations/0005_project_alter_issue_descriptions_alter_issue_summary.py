# Generated by Django 5.0 on 2023-12-27 16:37

import webapp.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_remove_issue_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('start_date', models.DateField(verbose_name='Дата начала')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата окончания')),
            ],
        ),
        migrations.AlterField(
            model_name='issue',
            name='descriptions',
            field=models.TextField(blank=True, null=True, validators=[webapp.validators.validate_descriptions_length], verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='summary',
            field=models.CharField(max_length=50, validators=[webapp.validators.validate_summary_not_empty], verbose_name='Краткое описание'),
        ),
    ]
