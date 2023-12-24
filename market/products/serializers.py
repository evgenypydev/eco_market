from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer
from .models import Product, Category


class ProductCRUDSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ["id", "title", "image", "capacity", "description", "price", "category"]


class CategoryCRUDSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "title", "image"]
