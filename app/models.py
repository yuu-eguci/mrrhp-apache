from django.db import models


class Config(models.Model):

    key = models.CharField(
        verbose_name='Config key name',
        max_length=30,
        blank=True,
        null=True,
        unique=True,
    )
    value = models.CharField(
        verbose_name='Config value',
        max_length=100,
        blank=True,
        null=True,
    )
