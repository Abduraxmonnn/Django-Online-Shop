# Django
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

# Project
from apps.features.components.models import Cpu, VideoCart
from apps.products.models import Product


class PCBuildFeature(models.Model):
    product = GenericRelation(Product, related_query_name='pc_build_feature')
    cpu = models.ForeignKey(Cpu, on_delete=models.SET_NULL, null=True)
    mb = models.CharField(max_length=50)
    ram = models.CharField(max_length=150)
    cooler = models.CharField(max_length=80)
    ssd = models.CharField(max_length=150, blank=True, null=True)
    hdd = models.CharField(max_length=150, blank=True, null=True)
    gpu = models.ForeignKey(VideoCart, on_delete=models.SET_NULL, null=True)
    psu = models.CharField(max_length=100)
    case = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cpu} - {self.ram} - {self.case}'

    class Meta:
        ordering = ('-id', )
