from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=25)
    last_updated = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'
