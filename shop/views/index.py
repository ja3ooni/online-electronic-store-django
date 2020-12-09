from django.views import View
from django.shortcuts import render
from shop.models import Category, Product, ShopCart

def index(request):
    current_user = request.user
    products = Product.objects.all()
    categories = Category.objects.all()
    carts = ShopCart.objects.filter(user_id=current_user.id)
    qty = 0
    for cart in carts:
        qty = qty + cart.qty
    params = {
        'products': products,
        'categories':categories,
        'qty':qty,
        'carts':carts,
        }
    return render(request, 'index.html', params)