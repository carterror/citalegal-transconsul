# Generated by Django 4.2.10 on 2024-09-03 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajador',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='trabajadores/', verbose_name='Foto de Trabajador'),
        ),
    ]