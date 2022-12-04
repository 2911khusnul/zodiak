# Generated by Django 4.1.1 on 2022-10-07 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_remove_artikel_kategori_artikel_host'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artikel',
            old_name='host',
            new_name='kategori',
        ),
        migrations.AddField(
            model_name='artikel',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
