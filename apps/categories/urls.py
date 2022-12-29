from django.conf.urls import include
from django.urls import path
from apps.categories.api.brand_categories import BrandCategoryViewSet
from apps.categories.api.product_categories import ProductCategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'brand', BrandCategoryViewSet, 'brand'),

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'product/detail/<int:pk>/', ProductCategoryViewSet.as_view())
]
