from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
import datetime

# Create your models here.

class KritikSaran(models.Model):
    nama = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pesan = models.CharField(max_length=255)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ['-updated', '-created']

    def __str__(self):
        return self.nama