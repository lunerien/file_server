from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    api_key = models.CharField(max_length=40, blank=True)


class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
