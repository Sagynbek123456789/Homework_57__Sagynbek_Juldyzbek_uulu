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
    summary = models.CharField(
        max_length=50,
        verbose_name='Краткое описание',
        validators=[validate_summary_not_empty]
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

    def __str__(self):
        return f'{self.id}. {self.summary}'