from django.shortcuts import render, get_object_or_404
from .models import Product


def list(request):
    product_list = Product.objects.all()
    context = {"product_list": product_list}

    return render(request, "product/product_list.html", context)

def detail(request, num):

    # product = Product.objects.get(id=num)
    product = get_object_or_404(Product, pk=num)

    context = {"product": product}
    return render(request, "product/product_detail.html", context)