from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class AccountUser(AbstractUser):
    avatar = models.ImageField(
        upload_to='authentication',
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=14,
        null=True
    )

    def __str__(self):
        return self.username
