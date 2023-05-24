from django.contrib import admin
from .models import * 
# Register your models here.

admin.site.register(category)
class ProductImageAdmin(admin.StackedInline):
    model = productImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]

admin.site.register(product, ProductAdmin)

admin.site.register(productImages)
admin.site.register(order)
admin.site.register(cart)