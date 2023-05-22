from django.shortcuts import render
from django.http import HttpResponse

from .models import product
from .models import category
# Create your views here.
def home(request):
    Products = product.objects.all()[:3]
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