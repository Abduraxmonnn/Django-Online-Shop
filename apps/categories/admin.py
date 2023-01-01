# Django
from django.contrib import admin

# Project
from apps.categories.models import ProductCategory


@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_updated']
    list_filter = ['name', 'last_updated', 'created_date']
    list_display_links = ['name', ]
    search_fields = ['name', ]
    ordering = ['name', ]
