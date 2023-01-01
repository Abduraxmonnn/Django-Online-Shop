# Django
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation

# Project
from apps.products.models import Product


class MouseFeature(models.Model):
    YES = 'YES'
    NO = 'NO'
    YesNoEnum = [
        (YES, 'YES'),
        (NO, 'NO')
    ]

    product = GenericRelation(Product, related_query_name='mouse_feature')
    sensor_type = models.CharField(max_length=100)
    dpi_cpi = models.IntegerField(verbose_name=_('Max DPI/CPI Resolution (Integer)'))
    num_buttons = models.IntegerField(verbose_name=_('Number of buttons (Integer)'))
    frequency = models.IntegerField(verbose_name=_('Polling frequency (Hz)'))
    acceleration = models.IntegerField(verbose_name=_('Acceleration (maximum acceleration) (Gram)'))
    blacklight = models.CharField(max_length=3, choices=YesNoEnum, default=YES)
    inner_memory = models.CharField(verbose_name=_('Inner memory'), max_length=3, choices=YesNoEnum, default=YES)
    working_mode = models.CharField(max_length=8)
    wire_type = models.CharField(max_length=70)
    total_weight = models.IntegerField(verbose_name=_('Weight with cable'))
    weight = models.IntegerField(verbose_name=_('Weight without cable'))
    dimensions = models.CharField(max_length=80)
    created_date = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.dpi_cpi}'

    class Meta:
        ordering = ('-id', )
