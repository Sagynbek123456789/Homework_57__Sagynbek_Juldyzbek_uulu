from django.contrib.auth import get_user_model
from django.db import models
from .validators import validate_summary_not_empty, validate_descriptions_length


class Status(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.title


class Type(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.title


class Issue(models.Model):
    summary = models.ForeignKey(
        get_user_model(),
        default=1,
        related_name='issue',
        on_delete=models.CASCADE,
        verbose_name='Название'
    )
    descriptions = models.TextField(
        null=True,
        blank=True,
        verbose_name='Полное описание',
        validators=[validate_descriptions_length]
    )
    status = models.ForeignKey(
        'webapp.Status',
        on_delete=models.RESTRICT,
        related_name='issues',
        verbose_name='Статус'
    )
    types = models.ManyToManyField(
        'webapp.Type',
        related_name='issues',
        verbose_name='Типы'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    project = models.ForeignKey('webapp.Project', on_delete=models.CASCADE, related_name='issues', verbose_name='Проект')

    def __str__(self):
        return f'{self.id}. {self.summary}'


class Project(models.Model):
    title = models.ForeignKey(get_user_model(), default=1, related_name='projects', on_delete=models.CASCADE, verbose_name='Название')
    descriptions = models.TextField(verbose_name='Описание')
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания', null=True, blank=True)

    def __str__(self):
        return f'{self.title} - {self.start_date} - {self.end_date}'

