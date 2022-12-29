# Rest Framework
from rest_framework import serializers

# Project
from apps.categories.models import BrandCategory


class BrandCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandCategory
        fields = [
            'name',
            'created_date'
        ]
