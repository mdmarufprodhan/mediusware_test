from django.contrib import admin
from .models import Product
admin.site.register(Product)
from .models import ProductVariantPrice
admin.site.register(ProductVariantPrice)
# Register your models here.


