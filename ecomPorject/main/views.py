from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

from .models import product
from .models import category
from .models import cart
from .models import order
from .models import productImages


@login_required
def home(request):
    current_user = request.user
    Products = product.objects.all()
    Categories = category.objects.all()
    CartProducts = cart.objects.filter(user = current_user)
    CartCount = CartProducts.count()
    totalPrice = 0
    for CartProduct in CartProducts:
        totalPrice += CartProduct.product.price

    context = {
        'Products':Products,
        'Categories':Categories,
        'CartProducts':CartProducts,
        'CartCount':CartCount,
        'totalPrice':totalPrice,
    }
    return render(request, 'index.html', context)

def shop(request):
    current_user = request.user
    Products = product.objects.all()
    Categories = category.objects.all()
    CartProducts = cart.objects.filter(user = current_user)
    CartCount = CartProducts.count()
    totalPrice = 0
    for CartProduct in CartProducts:
        totalPrice += CartProduct.product.price
    context = {
        'Products':Products,
        'Categories':Categories,
        'CartCount':CartCount,
        'CartProducts':CartProducts,
        'totalPrice':totalPrice,
    }
    return render(request, 'store.html', context)

def shopByCategory(request):
    if request.method == 'POST':
        ctg_id = request.POST.get('ctg_id')
        lable = 0
        if ctg_id == '0':
            Products = product.objects.all()
            Categories = category.objects.all()
            lable = 0
            context = {
            'Products':Products,
            'Categories':Categories,
            'lable':lable,
            }
            return render(request, 'store.html', context)
        else:
            Category = category.objects.get(id = ctg_id)
            Products = product.objects.filter(category = Category)
            Categories = category.objects.all()
            lable = ctg_id
            context = {
                'Products':Products,
                'Categories':Categories,
                'lable':lable,
            }
            return render(request, 'store.html', context)

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
    current_user = request.user
    UserCart = cart.objects.filter(user = current_user)
    totalPrice = 0
    for order in UserCart:
        totalPrice += order.product.price
    context = {
        'UserCart':UserCart,
        'totalPrice':totalPrice,
    }
    return render(request, 'checkout.html', context)

def ProductDetails(request, id):
    Product = product.objects.get(id = id)
    ProductImages = productImages.objects.filter(product = Product)
    context = {
        'Product':Product,
        'ProductImages':ProductImages,
    }
    return render(request, 'product.html', context)


def PlaceOrder(request):
    if request.method == 'POST':
        current_user = request.user
        zip_code = request.POST.get('zip_code')
        address = request.POST.get('address')
        paymentMethod = request.POST.get('paymentMethod')
        NewOrder = order.objects.create(
            user = current_user,
            address = address,
            Payment_method = paymentMethod,
            postel_code = zip_code
        )
        NewOrder.save()

        UserCart = cart.objects.filter(user = current_user)
        for Cart in UserCart:
            NewOrder.product.add(Cart.product)
        
        NewOrder.save()
        messages.success(request, "Order have been blaced successfully!")
        return redirect('checkOut')
    
def OrderList(request):
    current_user = request.user
    UserOrderList = order.objects.filter(user = current_user)
    context = {
        'UserOrderList':UserOrderList,
    }

    return render(request, 'order.html', context)