from django.db import models
from products.models import Product
from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
    phone_number = PhoneNumberField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    landmark = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    total_price = models.FloatField(null=True, blank=True)
    delivery_price = models.FloatField(null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - Total Price: {self.total_price}"


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Order #{self.order_id.id} - {self.product_id.title} - Quantity: {self.quantity}"
