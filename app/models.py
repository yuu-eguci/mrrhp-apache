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


class Tag(models.Model):

    code = models.CharField(
        verbose_name='Tag code, used for url for example',
        max_length=20,
        blank=False,
        null=False,
        unique=True,
    )

    name_ja = models.CharField(
        verbose_name='Tag name in Japanese',
        max_length=20,
        blank=False,
        null=False,
    )

    name_en = models.CharField(
        verbose_name='Tag name in English',
        max_length=20,
        blank=False,
        null=False,
    )


class Year(models.Model):

    code = models.CharField(
        verbose_name='Year code, used for url for example',
        max_length=20,
        blank=False,
        null=False,
        unique=True,
    )
