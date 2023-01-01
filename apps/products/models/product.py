# Django
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Project
from apps.categories.models.category import ProductCategory
from apps.brands.models.brand import Brand


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    brand = models.ManyToManyField(Brand)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    feature = GenericForeignKey('content_type', 'object_id')

    price = models.FloatField()
    color = models.CharField(max_length=50)
    description = models.TextField()
    image1 = models.ImageField(upload_to='images/products/%Y/%m')
    image2 = models.ImageField(upload_to='images/products/%Y/%m')
    image3 = models.ImageField(upload_to='images/products/%Y/%m', blank=True, null=True)
    image4 = models.ImageField(upload_to='images/products/%Y/%m', blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-id', )
