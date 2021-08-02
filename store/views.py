from django.shortcuts import get_object_or_404, redirect, render

from .models import Category, Product


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


def category_list(request, category_slug=None):
    # category = get_object_or_404(Category, slug=category_slug)
    category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    # product = get_object_or_404(Product, slug=slug, in_stock=True)
    # product = Product.objects.get(slug=slug)
    product = Product.objects.all().filter(slug=slug).get()
    return render(request, 'store/products/detail.html', {'product': product})

def search_result(request):
    slug=request.GET['searchtext']    
    category = Category.objects.filter(slug=slug)
    product = Product.objects.filter(slug=slug)
    if category:
        return redirect('category/'+slug)
    elif product:
        return redirect('product/'+slug)
    else:     
        return render(request, 'store/notfound.html', {'searchtext': slug})      