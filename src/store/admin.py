from django.contrib import admin
from accounts.models import Shopper
from store.models import Cart, Order, Product,Size

# Register your models here.
admin.site.register(Product)
admin.site.register(Shopper)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Size)