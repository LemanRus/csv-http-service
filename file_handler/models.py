from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser):
    groups = None
    objects = UserManager()


class CSVFile(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField()

