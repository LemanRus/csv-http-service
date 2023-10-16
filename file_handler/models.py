from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser):
    groups = None
    objects = UserManager()
