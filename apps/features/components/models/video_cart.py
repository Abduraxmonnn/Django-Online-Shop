# Django
from django.db import models


class VideoCart(models.Model):
    name = models.CharField(max_length=150, unique=True)
    created_date = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id', )
