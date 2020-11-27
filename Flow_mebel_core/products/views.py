from django.shortcuts import redirect, render
from .models import Product
from .forms import RegistrationForm

# Create your views here.
def get_all(request):
    products = Product.objects.all()
    context = {
        'items': products
    }
    return render(request=request, template_name='products/products.html', context=context)

def register(request):
    form = RegistrationForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect('products')