from django.shortcuts import render

from .models import Category, Product


def main_page(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {

        'categories': categories,
        'products': products,

    }
    return render(request, 'main_page.html', context)
# Create your views here.
