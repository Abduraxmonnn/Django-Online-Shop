# Django
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

# Project
from apps.features.components.models import Cpu, VideoCart
from apps.products.models import Product


class LaptopFeature(models.Model):
    product = GenericRelation(Product, related_query_name='laptop_feature')
    cpu = models.ForeignKey(Cpu, on_delete=models.SET_NULL, null=True)
    ram = models.CharField(max_length=150)
    storage = models.CharField(max_length=200)
    video_cart = models.ForeignKey(VideoCart, on_delete=models.SET_NULL, null=True)
    screen = models.CharField(max_length=250)
    extra = models.TextField()
    network = models.CharField(max_length=100)
    keyboard = models.CharField(max_length=50)
    frame = models.CharField(max_length=50)
    web_camera = models.CharField(max_length=50)
    ports = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cpu} - {self.ram} - {self.storage}'

    class Meta:
        ordering = ('-id', )
