from django.views import View
from django.shortcuts import render
from shop.models import Category, Product, ShopCart

def index(request):
    current_user = request.user
    products = Product.objects.all()
    mobiles = Product.objects.filter(category_id=1)
    laptops = Product.objects.filter(category_id=2)
    tvs = Product.objects.filter(category_id=3)
    headphones = Product.objects.filter(category_id=6)
    homeapps = Product.objects.filter(category_id=9)
    kitapps = Product.objects.filter(category_id=8)
    categories = Category.objects.all()
    carts = ShopCart.objects.filter(user_id=current_user.id)
    qty = 0
    for cart in carts:
        qty = qty + cart.qty
    params = {
        'products': products[:8],
        'mobiles': mobiles,
        'laptops': laptops,
        'tvs': tvs,
        'headphones': headphones,
        'homeapps': homeapps,
        'kitapps': kitapps,
        'categories':categories,
        'qty':qty,
        'carts':carts,
        }
    return render(request, 'index.html', params)