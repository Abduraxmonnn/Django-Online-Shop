from django.contrib import admin

# Register your models here.
from apps.brands.models.brand import Brand

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'last_updated']
    list_filter = ['name', 'last_updated', 'created_date']
    list_display_links = ['name', ]
    search_fields = ['name', ]
    ordering = ['name', ]
