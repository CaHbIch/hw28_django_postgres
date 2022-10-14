from django.db import models
from django.utils import timezone


class Ad(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    time_create = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
