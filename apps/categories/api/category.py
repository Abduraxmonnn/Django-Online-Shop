# Rest Framework
from rest_framework import viewsets

# Project
from apps.categories.models.category import ProductCategory
from apps.categories.serializers.category import ProductCategorySerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    filter_fields = ['name', 'created_date']
    search_fields = ['name', ]
    ordering_fields = ['-id', 'name', 'created_date']
