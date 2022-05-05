from django.shortcuts import render

from .models import Category, Product


def main_page(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    print(request.POST)
    if request.method == 'POST':
        product = Product.objects.filter(title=request.POST.get('find'))
        #disc = Product.objects.get(discription = product)
        print(product)
        if product:
            context = {
                'product': product,
                'categories': categories,
            }
            return render(request, 'main_page.html', context)

        else:
            context = {
                'error': 'Поиск не дал результатов',
                'categories': categories,
            }
            return render(request, 'main_page.html', context)
    context = {

        'categories': categories,
        'products': products,

    }
    return render(request, 'main_page.html', context)
# Create your views here.
