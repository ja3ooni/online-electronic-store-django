from shop.models import Category, ShopCart
from django.shortcuts import render

def contact(request):
    current_user = request.user
    carts = ShopCart.objects.filter(user_id=current_user.id)
    categories = Category.objects.all()
    qty = 0
    for cart in carts:
        qty = qty + cart.qty
    return render(request, 'contactus.html', {'qty':qty, 'categories':categories})