from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['product_id', 'quantity']


class OrderCreateUpdateSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, required=True)

    class Meta:
        model = Order
        fields = ["id", "order_items", "phone_number", "address", "landmark", "comment", "total_price",
                  "delivery_price", "order_date"]

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        for order_item_data in order_items_data:
            OrderItem.objects.create(order_id=order, **order_item_data)
        return order

    def update(self, instance, validated_data):
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.address = validated_data.get('address', instance.address)
        instance.landmark = validated_data.get('landmark', instance.landmark)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.delivery_price = validated_data.get('delivery_price', instance.delivery_price)
        instance.total_price = (sum(item.product_id.price * item.quantity for item in instance.order_items.all() if
                                item.product_id.price is not None) +
                                (instance.delivery_price if instance.delivery_price is not None else 0))

        instance.save()

        return instance


class OrderListRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ["id", "order_items", "phone_number", "address", "landmark", "comment", "total_price",
                  "delivery_price", "order_date"]

