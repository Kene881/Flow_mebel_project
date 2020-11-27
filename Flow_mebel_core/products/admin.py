from django.contrib import admin
from .models import Product, Image_for_prod

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'cost')
    search_fields = ['title']
    list_filter = ('title',)

admin.site.register(Image_for_prod)