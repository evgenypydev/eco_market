from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .endpoints import ProductViewSet, CategoryViewSet

router_products = DefaultRouter()
router_products.register(r'', ProductViewSet)

router_categories = DefaultRouter()
router_categories.register(r'', CategoryViewSet)

urlpatterns = [
    path('products/', include(router_products.urls)),
    path('categories/', include(router_categories.urls)),
]
