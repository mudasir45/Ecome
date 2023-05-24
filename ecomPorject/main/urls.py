from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('shorByCategory/<int:ctg_id>', views.shorByCategory, name='shorByCategory'),
    path('addToCart/', views.addToCart, name='addToCart'),
]
