from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

from .models import product
from .models import category
from .models import cart
from .models import order


@login_required
def home(request):
    current_user = request.user
    Products = product.objects.all()
    Categories = category.objects.all()
    CartProducts = cart.objects.filter(user = current_user)
    CartCount = CartProducts.count()

    context = {
        'Products':Products,
        'Categories':Categories,
        'CartProducts':CartProducts,
        'CartCount':CartCount,
    }
    return render(request, 'index.html', context)

def shop(request):
    Products = product.objects.all()
    Categories = category.objects.all()
    context = {
        'Products':Products,
        'Categories':Categories
    }
    return render(request, 'shop.html', context)

def shorByCategory(request, ctg_id):
    Category = category.objects.get(id = ctg_id)
    Products = product.objects.filter(category = Category)
    Categories = category.objects.all()
    context = {
        'Products':Products,
        'Categories':Categories
    }
    return render(request, 'shop.html', context)

def addToCart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        Product = product.objects.get(id = product_id)
        current_user = request.user
        CartCount = cart.objects.filter(user = request.user).count()
        
        Cart, get = cart.objects.get_or_create(user = current_user, product = Product)
        Cart.save()
        data = {
            'message':'Add to cart done',
            'CartCount':CartCount,
        }
        return JsonResponse(data)
    
def checkOut(request):

    return render(request, 'checkout.html')