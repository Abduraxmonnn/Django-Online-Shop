# Django
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation

# Project
from apps.products.models import Product


class EarphoneFeature(models.Model):
    YES = 'YES'
    NO = 'NO'
    YesNoEnum = [
        (YES, 'YES'),
        (NO, 'NO')
    ]

    product = GenericRelation(Product, related_query_name='ear_phone_feature')
    type = models.CharField(max_length=50)
    working_mode = models.CharField(max_length=50)
    sound_type = models.CharField(max_length=30)
    speaker_size = models.IntegerField(verbose_name=_('Speaker size (mm)'))
    frequency_range = models.CharField(verbose_name=_('Earphone frequency range (Hz)'), max_length=20)
    impedance = models.IntegerField(verbose_name=_('Earphone impedance (ohm)'))
    sensitivity = models.IntegerField(verbose_name=_('Earphone sensitivity (dB)'))
    microphone_frequency_range = models.CharField(verbose_name=_('Microphone frequency range'), max_length=20)
    microphone_sensitivity = models.CharField(verbose_name=_('Microphone sensitivity (dB)'), max_length=15)
    connection = models.CharField(verbose_name=_('Connection, connectors'), max_length=15)
    sound_card = models.CharField(verbose_name=_('Sound card'), max_length=3, choices=YesNoEnum, default=NO)
    wire_length = models.IntegerField(verbose_name=_('Wire length (Meter)'))
    blacklight = models.CharField(max_length=3, choices=YesNoEnum, default=NO)
    weight = models.IntegerField(verbose_name=_('Weight (Gram)'))
    created_date = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.type} - {self.working_mode} = {self.connection}'

    class Meta:
        ordering = ('-id', )
