from django.contrib import admin

# Register your models here.
from apps.products.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'price', 'color')
    list_filter = ('name', 'price', 'category__name', 'brand__name')
    list_display_links = ('name', 'category', 'price')
    search_fields = ('name', 'brand')
    ordering = ('name', )
