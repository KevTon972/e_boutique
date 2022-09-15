
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from store.models import Cart, Order, Product, Size
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F, Sum


def index(request):
    products = Product.objects.all()

    return render(request, 'store/index.html', context={'products': products})

def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
        
    return render(request, 'store/product_details.html', context={'product': product, 'sizes': Size.objects.all()})
     

def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug,)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, product=product)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()
    
    return redirect(reverse("product", kwargs={"slug":slug}))

def cart(request):
    cart = get_object_or_404(Cart, user=request.user) 
    total_price = 0
    for order in cart.orders.all():
        total_price = total_price + order.product.price * order.quantity
    
    order_price = order.product.price * order.quantity
    

    return render(request, 'store/cart.html', context={"orders":cart.orders.all(), "order_price": order_price, "total_price": total_price})


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
    return render(request, 'store/cart.html', context={"orders":cart.orders.all()})
