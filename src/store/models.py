from django.db import models
from django.urls import reverse
from e_boutique.settings import AUTH_USER_MODEL

class Size(models.Model):
    size = models.IntegerField(default=39)
    
    def __str__(self):
        return f"{self.size}"

class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128)
    sizes = models.ManyToManyField(Size)
    price = models.FloatField(default=0.00)
    stock = models.IntegerField(default=0)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse('product', kwargs={"slug":self.slug})


class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0.00)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name}, {self.size} ({self.quantity})"

class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username
