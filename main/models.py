from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    STATUS_CHOICES = [
        ('regular', 'Regular'),
        ('advanced', 'Advanced'),
        ('vip', 'VIP'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='regular',
    )

    def __str__(self):
        return self.username
