from django.shortcuts import redirect, render
from .models import Product, Image_for_prod
from .forms import OrderForm

# Create your views here.
def get_all(request):
    products = Product.objects.all()
    context = {
        'items': products
    }
    return render(request=request, template_name='products/products.html', context=context)


def create(request, id): 
    form = OrderForm(request.POST, request.FILES)
    if form.is_valid():
        order = form.save(commit=False)
        order.product = Product.objects.get(pk=id)
        order.save()
        form.save_m2m()
    return redirect('products')

def detail_prod(request, id):
    p = Product.objects.get(pk = id)
    all_images = Image_for_prod.objects.all().filter(product = p)
    context = {
        'product': p,
        'images': all_images,
        'OrderForm':OrderForm()
    }
    return render(request,'products/details.html', context=context)