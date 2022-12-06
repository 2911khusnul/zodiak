# Generated by Django 4.1.3 on 2022-12-06 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_komentar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zodiak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_zodiak', models.CharField(max_length=255)),
                ('tanggal', models.CharField(max_length=255)),
                ('simbol', models.CharField(max_length=255)),
                ('deskripsi', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]