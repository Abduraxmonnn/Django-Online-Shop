from django.db import models


class BrandCategory(models.Model):
    name = models.CharField(max_length=50)
    last_updated = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brand Category'
        verbose_name_plural = 'Brand Categories'
