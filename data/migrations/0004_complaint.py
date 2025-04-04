# Generated by Django 5.1.6 on 2025-04-02 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('selesai', 'Selesai'), ('progress', 'Dalam Progress'), ('tidak_valid', 'Tidak Valid'), ('sudah_dibaca', 'Sudah Dibaca'), ('pending', 'Menunggu Konfirmasi')], default='pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
