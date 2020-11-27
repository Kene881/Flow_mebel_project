from django.contrib import admin
from .models import Product
from .models import Order
from .models import Image_for_prod

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'cost')
    search_fields = ['title']
    list_filter = ('title',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'product', 'size', 'material')
    search_fields = ['first_name']
    list_filter = ('first_name',)

@admin.register(Image_for_prod)
class Image_for_prodAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
    search_fields = ['product']
    list_filter = ('product',)
