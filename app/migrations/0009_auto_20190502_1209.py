# Generated by Django 2.1.8 on 2019-05-02 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='count',
            field=models.IntegerField(blank=True, null=True, verbose_name='How many posts belongs to this tag.'),
        ),
        migrations.AddField(
            model_name='year',
            name='count',
            field=models.IntegerField(blank=True, null=True, verbose_name='How many posts belongs to this year.'),
        ),
        migrations.AlterField(
            model_name='post',
            name='year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Year', verbose_name='Year for this post'),
        ),
    ]
