# Generated by Django 3.1.3 on 2020-11-15 06:50

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20201114_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
