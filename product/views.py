from django.shortcuts import render
from .models import Product


def list(request):
    product_list = Product.objects.all()
    context = {"product_list": product_list}

    return render(request, "product/product_list.html", context)

def detail(request, num = 1):
    product = Product.objects.get(id=num)
    context = {"product": product}
    return render(request, "product/product_detail.html", context)