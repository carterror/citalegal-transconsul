# Generated by Django 4.2.10 on 2024-06-19 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('cuerpo', models.TextField()),
                ('presentar', models.BooleanField(blank=True, default=True)),
                ('publicado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
