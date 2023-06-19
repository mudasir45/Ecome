from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User


class product(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    discription = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey('category', on_delete=models.CASCADE, null=True, blank=True)
    img = models.ImageField(upload_to="product", null=True, blank=True)
    price = models.IntegerField()
    tag = models.CharField(max_length=20, null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title

class category(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="category")


    def __str__(self) -> str:
        return self.name

class productImages(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to="product")

class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(product, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.user.username} --> {self.product.title}'

STATUS_CHOICES = (
    ('complete', 'complete'),
    ('pending', 'pending'),
    ('cancel', 'cancel'),
)
class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ManyToManyField(product)
    address = models.CharField(max_length=50, null=True, blank=True)
    Payment_method = models.CharField(max_length=100, null=True, blank=True)
    postel_code = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default='pending')

    def __str__(self) -> str:
        return f'{self.user.username} - {self.status}'