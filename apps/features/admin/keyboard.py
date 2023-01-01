# Django
from django.contrib import admin

# Project
from apps.features.models import KeyboardFeature


@admin.register(KeyboardFeature)
class KeyboardFeatureAdmin(admin.ModelAdmin):
    list_display = ['type', 'switch_type', 'interface', 'cabling', 'weight']
    list_filter = ['type', 'switch_type', 'cabling']
    list_display_links = ['type', 'switch_type', 'cabling']
    search_fields = ['type', ]
    ordering = ['type', ]
