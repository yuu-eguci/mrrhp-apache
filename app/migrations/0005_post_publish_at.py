# Generated by Django 2.1.8 on 2019-04-27 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publish_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date to publish'),
        ),
    ]
