from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


from .models import product
from .models import category
from .models import cart
from .models import order


def home(request):
    Products = product.objects.all()
    Categories = category.objects.all()

    context = {
        'Products':Products,
        'Categories':Categories
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
        
        Cart, get = cart.objects.get_or_create(user = current_user, product = Product)
        Cart.save()
        data = {
            'message':"Add to cart done"
        }
        return JsonResponse(data)
    