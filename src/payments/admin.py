from django.contrib import admin
from payments.models import Price, Product
# Register your models here.
admin.site.register(Product)
admin.site.register(Price)