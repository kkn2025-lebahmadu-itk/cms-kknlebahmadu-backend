# Generated by Django 5.1.6 on 2025-05-27 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0015_letterrecap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='pdf',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
