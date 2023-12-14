from django.db import models

class Category(models.Model):
    categories = [
        ("fruits", "fruits"),
        ("dried fruit", "dried fruit"),
        ("vegetables", "vegetables"),
        ("greens", "greens"),
        ("tea coffee", "tea coffee"),
        ("milk products", "milk products"),
    ]
    title = models.CharField(choices=categories, max_length=15)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    title = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()
    description = models.TextField(max_length=150)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.capacity} - {self.price}"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
