from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# Create your views here.

def home_view(request):
    return render(request, 'home.html')

# Create View
def create_product_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'product-form.html', {'form': form})

# Read View
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'product-list.html', {'products': products})

# Update View
def update_product_view(request,pid):
    product= Product.objects.get(product_id=pid)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'product-form.html', {'form': form})

# Delete View
def delete_product_view(request,pid):
    product= Product.objects.get(product_id=pid)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product-delete.html', {'product': product})