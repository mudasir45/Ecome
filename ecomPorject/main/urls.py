from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('shopByCategory/', views.shopByCategory, name='shopByCategory'),
    path('addToCart/', views.addToCart, name='addToCart'),
    path('checkOut/', views.checkOut, name='checkOut'),
]
