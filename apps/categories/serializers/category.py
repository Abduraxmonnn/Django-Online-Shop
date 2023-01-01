# Rest Framework
from rest_framework import serializers

# Project
from apps.categories.models.category import ProductCategory


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = [
            'name',
            'created_date'
        ]
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.last_update = validated_data.get("last_update", instance.last_update)
        instance.created_date = validated_data.get("created_date", instance.created_date)
        instance.save()
        return super(ProductCategory).update(instance, validated_data) # or return instance
