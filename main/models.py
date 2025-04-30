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


# models.py
class Course(models.Model):
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=50)
    is_free = models.BooleanField(default=False)
    rating = models.FloatField(default=0)
    duration = models.CharField(max_length=50)  # например, "3 сағ"
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
