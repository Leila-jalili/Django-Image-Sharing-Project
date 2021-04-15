from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
# Create your views here.

def products_view(request):
    products = Product.objects.all()
    context = {
        "products": products

    }
    return render(request, "products.html", context)

def product_create_view(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")

    return render(request, "product_create.html", {"form": form})   


def product_details_view(request, id):
    product = get_object_or_404(Product, pk=id)  
    return render(request, "product_details.html", {"product": product})  
