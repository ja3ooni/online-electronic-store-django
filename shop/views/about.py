from shop.models import Category, ShopCart
from django.shortcuts import render

def about(request):
    current_user = request.user
    catgories = Category.objects.all()
    carts = ShopCart.objects.filter(user_id=current_user.id)
    qty = 0
    for cart in carts:
        qty = qty + cart.qty
    return render(request, 'about.html', {'qty':qty, 'categories':catgories})