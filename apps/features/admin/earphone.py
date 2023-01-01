# Django
from django.contrib import admin

# Project
from apps.features.models import EarphoneFeature


@admin.register(EarphoneFeature)
class EarphoneFeatureAdmin(admin.ModelAdmin):
    list_display = ['type', 'working_mode', 'weight', 'connection']
    list_filter = ['type', 'working_mode', 'connection']
    list_display_links = ['type', 'working_mode']
    search_fields = ['type', ]
    ordering = ['type', ]
