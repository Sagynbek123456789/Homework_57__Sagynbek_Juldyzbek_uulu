from django.db import models


# Create your models here.
class Status(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.title


class Type(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.title


class Issue(models.Model):
    summary = models.CharField(max_length=50, verbose_name='Краткое описание')
    descriptions = models.TextField(null=True, blank=True, verbose_name='Полное описание')
    status = models.ForeignKey('webapp.Status', on_delete=models.RESTRICT, verbose_name='Статус')
    type = models.ForeignKey('webapp.Type', on_delete=models.RESTRICT, verbose_name='Тип')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    def __str__(self):
        return f'{self.id}. {self.summary}'

