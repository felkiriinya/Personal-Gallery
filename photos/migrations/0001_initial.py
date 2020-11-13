# Generated by Django 3.1.3 on 2020-11-13 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/')),
                ('image_name', models.CharField(max_length=60)),
                ('image_description', models.TextField()),
                ('image_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.category')),
                ('image_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.location')),
            ],
        ),
    ]