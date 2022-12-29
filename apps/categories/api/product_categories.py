# Django
from django_filters.rest_framework import DjangoFilterBackend

# Rest Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import views
from rest_framework.response import Response

# Project
from apps.categories.models.product_category import ProductCategory
from apps.categories.serializers.product_categories import ProductCategorySerializer


class ProductCategoryViewSet(views.APIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['name', 'created_date']
    search_fields = ['name', ]
    ordering_fields = ['-id', 'name', 'created_date']

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response("error")

        try:
            instance = ProductCategory.objects.get(pk=pk)
        except:
            return Response("error")
        
        serializer = ProductCategorySerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"put": serializer.data})
