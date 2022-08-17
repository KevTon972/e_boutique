from django.urls import path
from store.views import delete_cart, delete_to_cart, index, product_details, add_to_cart, cart

urlpatterns = [
    path('', index, name='index'),
    path('product/<str:slug>/', product_details, name='product'),
    path('product/<str:slug>/add-to-cart/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    path('cart/delete_cart/', delete_cart, name='delete_cart'),
    path('cart/delete_to_cart/<int:pk>/', delete_to_cart, name='delete_to_cart'),
]