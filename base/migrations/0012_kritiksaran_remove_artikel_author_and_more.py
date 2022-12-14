# Generated by Django 4.1.3 on 2022-12-05 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_kategoriresep'),
    ]

    operations = [
        migrations.CreateModel(
            name='KritikSaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('pesan', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='artikel',
            name='author',
        ),
        migrations.RemoveField(
            model_name='artikel',
            name='kategori_artikel',
        ),
        migrations.DeleteModel(
            name='KategoriResep',
        ),
        migrations.RemoveField(
            model_name='produk',
            name='author',
        ),
        migrations.RemoveField(
            model_name='produk',
            name='kategori_produk',
        ),
        migrations.DeleteModel(
            name='Setting',
        ),
        migrations.DeleteModel(
            name='Slider',
        ),
        migrations.DeleteModel(
            name='Artikel',
        ),
        migrations.DeleteModel(
            name='KategoriArtikel',
        ),
        migrations.DeleteModel(
            name='KategoriProduk',
        ),
        migrations.DeleteModel(
            name='Produk',
        ),
    ]
