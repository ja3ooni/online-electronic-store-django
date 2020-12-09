from shop.models import ShopCart
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='/login')
def cart(request):
    currentuser = request.user
    shopcarts = ShopCart.objects.filter(user_id=currentuser.id)

    total = 0
    qty = 0
    for shopcart in shopcarts:
        total = total + shopcart.amount
        qty = qty + shopcart.qty
    
    discount = 10/100 * total
    if discount > 20000:
        discount = 20000

    grand_total = total - discount
    
    cart = {
        'shopcarts':shopcarts,
        'qty':qty,
        'total':total,
        'discount':discount,
        'grand_total':grand_total,
    }
    
    return render(request, 'cart.html', cart)