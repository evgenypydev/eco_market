from django.db import models

from products.models import Product


class Order(models.Model):
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    landmark = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_price = models.FloatField()
    delivery_price = models.FloatField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - Total Price: {self.total_price}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Order #{self.order.id} - {self.product.title} - Quantity: {self.quantity}"
