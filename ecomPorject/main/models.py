from django.db import models
from django.utils.text import slugify


class product(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    discription = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey('category', on_delete=models.CASCADE, null=True, blank=True)
    img = models.ImageField(upload_to="product", null=True, blank=True)
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.title

class category(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="category")


    def __str__(self) -> str:
        return self.name


