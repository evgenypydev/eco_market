from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer
from .models import Product, Category

class ProductCRUDSerializer(ModelSerializer):
    category = StringRelatedField()

    class Meta:
        model = Product
        fields = ["id", "title", "capacity", "description", "price", "category"]

class CategoryCRUDSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "title"]
