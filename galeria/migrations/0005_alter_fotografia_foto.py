# Generated by Django 4.2.6 on 2023-11-07 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0004_fotografia_data_fotografia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='foto',
            field=models.FilePathField(),
        ),
    ]
