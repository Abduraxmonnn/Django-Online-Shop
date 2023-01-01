# Django
from django.contrib import admin

# Project
from apps.features.models import ArmChairFeature


@admin.register(ArmChairFeature)
class ArmChairFeatureAdmin(admin.ModelAdmin):
    list_display = ['type', 'color', 'permissible_load', 'frame_material']
    list_filter = ['type', 'permissible_load', 'frame_material']
    list_display_links = ['type', 'permissible_load', 'frame_material']
    search_fields = ['type', ]
    ordering = ['type', ]
