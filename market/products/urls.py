from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .endpoints import ProductViewSet, CategoryViewSet

product_router = DefaultRouter()
product_router.register(r'', ProductViewSet, basename='product')

category_router = DefaultRouter()
category_router.register(r'', CategoryViewSet, basename='category')

urlpatterns = [
    path("products/", include(product_router.urls)),
    path("categories/", include(category_router.urls)),
]
