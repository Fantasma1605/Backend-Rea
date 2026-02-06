from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = (
        ("owner", "Propriétaire"),
        ("tenant", "Locataire"),
        ("admin", "Admin"),
    )

    phone = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        null=True,
        blank=True
    )

    coins = models.IntegerField(default=0)

    is_kyc_verified = models.BooleanField(default=False)

    security_score = models.FloatField(default=0)

    def __str__(self):
        return self.username
