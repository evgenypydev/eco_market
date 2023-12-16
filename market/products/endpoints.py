from rest_framework.viewsets import ModelViewSet

from .models import Product, Category
from .serializers import ProductCRUDSerializer, CategoryCRUDSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductCRUDSerializer
    queryset = Product.objects.all()


class CategoryViewSet(ModelViewSet):
    serializer_class = CategoryCRUDSerializer
    queryset = Category.objects.all()