# Generated by Django 2.1.8 on 2019-04-26 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True, verbose_name='Tag code, used for url for example')),
                ('name_ja', models.CharField(max_length=20, verbose_name='Tag name in Japanese')),
                ('name_en', models.CharField(max_length=20, verbose_name='Tag name in English')),
            ],
        ),
    ]
