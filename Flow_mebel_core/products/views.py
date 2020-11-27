from django.shortcuts import redirect, render
from .models import Product

# Create your views here.
def get_all(request):
    products = Product.objects.all()
    context = {
        'items': products
    }
    return render(request=request, template_name='products/products.html', context=context)