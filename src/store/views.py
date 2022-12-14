
import json
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from store.models import Cart, Order, Product, Size
from django.http import JsonResponse

def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', context={'products': products})

def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    sizes = Size.objects.all()        
    return render(request, 'store/product_details.html', context={'product': product, 'sizes': sizes})
     
def add_to_cart(request, slug):
    if request.is_ajax():
        user = request.user
        ajax_response = request.GET.get('size')
        size = get_object_or_404(Size, size=ajax_response)
        product = get_object_or_404(Product, slug=slug)

        cart, _ = Cart.objects.get_or_create(user=user)   
        order, created = Order.objects.get_or_create(user=user, product=product, price=product.price, size=size)

        if created:
            cart.orders.add(order)
            cart.save()
        else:
            order.price += product.price
            order.quantity += 1
            order.save()
            
    return redirect(reverse("product", kwargs={"slug":slug}))

def cart(request):
    cart = get_object_or_404(Cart, user=request.user)    
    if cart:
        total_price = 0
        for order in cart.orders.all():
            total_price += order.price

        return render(request, 'store/cart.html', context={"orders":cart.orders.all(), "total_price": total_price})

def delete_cart(request):
    # delete the cart
    if cart := request.user.cart:
        cart.orders.all().delete()
        cart.delete()

    return redirect('index')

def delete_to_cart(request, pk):
    #remove an item from the cart
    user = request.user    
    if cart := user.cart:
        cart.orders.remove(pk)
        Order.objects.get(pk=pk).delete()   

    return redirect('cart')
