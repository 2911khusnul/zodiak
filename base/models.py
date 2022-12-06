from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
import datetime

# Create your models here.

class KritikSaran(models.Model):
    nama = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pesan = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ['-updated', '-created']

    def __str__(self):
        return self.nama


class Zodiak(models.Model):
    nama_zodiak = models.CharField(max_length=255)
    tanggal = models.CharField(max_length=255)
    simbol = models.CharField(max_length=255)
    deskripsi = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ['-updated', '-created']

    def __str__(self):
        return self.nama_zodiak

class Komentar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    zodiak = models.CharField(max_length=255)
    ramalan = models.CharField(max_length=255)
    komentar = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ['-updated', '-created']

    def __str__(self):
        return self.komentar