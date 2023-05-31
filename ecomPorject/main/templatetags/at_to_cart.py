from django import template
from django.template import Library
from main.models import *
from django.contrib.auth.models import User

register = Library()

@register.filter
# check user has done add to cart or not 
def checkAdToCart(product_id, user_id):
    Product = product.objects.get(id = product_id)
    user = User.objects.get(id = user_id)
    return cart.objects.filter(product = Product, user = user).exists()


