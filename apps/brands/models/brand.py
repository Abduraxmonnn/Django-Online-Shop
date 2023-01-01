# Django
from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=70, unique=True)
    created_date = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id',)
