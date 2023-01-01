# Django
from django.contrib import admin

# Project
from apps.features.models import LaptopFeature


@admin.register(LaptopFeature)
class LaptopFeatureAdmin(admin.ModelAdmin):
    list_display = ['cpu', 'ram', 'storage', 'video_cart', 'frame']
    list_filter = ['cpu', 'ram', ]
    list_display_links = ['cpu', 'ram', 'video_cart']
    search_fields = ['video_cart', 'ram', 'cpu']
    ordering = ['-id', ]
