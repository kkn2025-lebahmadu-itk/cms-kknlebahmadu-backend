# Generated by Django 5.1.6 on 2025-04-03 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
