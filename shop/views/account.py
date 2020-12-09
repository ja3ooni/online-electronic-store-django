from shop.models import Category, Customer, Order, OrderProduct, ShopCart, Wishlist
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User

@login_required(login_url='/login')
def account(request):
    orderprs=[]
    currentuser = request.user

    carts = ShopCart.objects.filter(user_id=currentuser.id)
    qty = 0
    for cart in carts:
        qty = qty + cart.qty
    
    categories = Category.objects.all()
    customer = Customer.objects.get(user_id=currentuser.id)
    wishlists = Wishlist.objects.filter(user_id=currentuser.id)

    orders = Order.objects.filter(user_id=currentuser.id)
    for order in orders:
        pr = OrderProduct.objects.filter(order_id=order.id)
        orderprs.append(pr)
    
    details = {
        'customer':customer,
        'orders':orders,
        'orderprs':orderprs,
        'qty':qty,
        'categories':categories,
        'wishlists':wishlists
        }

    return render(request, 'account.html', details)