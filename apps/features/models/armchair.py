# Django
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation

# Project
from apps.products.models import Product


class ArmChairFeature(models.Model):
    product = GenericRelation(Product, related_query_name='arm_chair_feature')
    type = models.CharField(max_length=70)
    upholstery_material = models.CharField(max_length=100)
    color = models.CharField(verbose_name=_('upholstery color'), max_length=100)
    armrests = models.CharField(max_length=30)
    cross_material = models.CharField(max_length=50)
    reclining = models.CharField(verbose_name=_('reclining the back (degree)'), max_length=100)
    permissible_load = models.CharField(verbose_name=_('Permissible load (kg)'), max_length=50)
    swing_mechanism = models.CharField(max_length=50)
    frame_material = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.type} - {self.color} - {self.reclining}'

    class Meta:
        ordering = ('-id', )
