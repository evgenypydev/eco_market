from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductCRUDSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductCRUDSerializer()

    class Meta:
        model = OrderItem
        fields = ["id", "order", "product", "quantity"]

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "phone_number", "address", "landmark", "comment", "products", "total_price", "delivery_price", "order_price"]