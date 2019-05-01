# Generated by Django 2.1.8 on 2019-04-30 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_post_html'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_at', models.DateTimeField(blank=True, null=True, verbose_name='Commented date')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Commenter name')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Body')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Post', verbose_name='属する記事')),
            ],
        ),
    ]