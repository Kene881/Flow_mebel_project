from django.contrib import admin
from .models import Product
from .models import Registration

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'cost')
    search_fields = ['title']
    list_filter = ('title',)

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email')
    search_fields = ['name']
    list_filter = ('name',)