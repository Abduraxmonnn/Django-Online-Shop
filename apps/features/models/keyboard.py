# Django
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation

# Project
from apps.products.models import Product


class KeyboardFeature(models.Model):
    YES = 'YES'
    NO = 'NO'
    YesNoEnum = [
        (YES, 'YES'),
        (NO, 'NO')
    ]

    product = GenericRelation(Product, related_query_name='keyboard_feature')
    type = models.CharField(max_length=100)
    switch_type = models.CharField(max_length=100)
    interface = models.CharField(max_length=30)
    backlight = models.CharField(max_length=50)
    num_key = models.IntegerField()
    wire_length = models.IntegerField(verbose_name=_('Wire length (meter)'))
    weight = models.IntegerField(verbose_name=_('Weight (gram)'))
    dimensions = models.CharField(max_length=50)
    cabling = models.CharField(max_length=3, choices=YesNoEnum, default=NO)
    inner_memory = models.CharField(max_length=3, choices=YesNoEnum, default=NO)
    palm_rest = models.CharField(max_length=3, choices=YesNoEnum, default=NO)
    created_date = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.type} - {self.interface}'

    class Meta:
        ordering = ('-id', )
