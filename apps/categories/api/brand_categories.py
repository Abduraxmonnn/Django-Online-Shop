# Django
from django_filters.rest_framework import DjangoFilterBackend

# Rest Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

# Project
from apps.categories.models.brand_category import BrandCategory
from apps.categories.serializers.brand_categories import BrandCategorySerializer


class BrandCategoryViewSet(ModelViewSet):
    queryset = BrandCategory.objects.all()
    serializer_class = BrandCategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['name', 'created_date']
    search_fields = ['name', ]
    ordering_fields = ['-id', 'name', 'created_date']
