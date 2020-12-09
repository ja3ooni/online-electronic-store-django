from django.contrib.auth.decorators import login_required
from django.contrib import messages
from shop.models import Customer, Order, OrderProduct, ShopCart
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string

@login_required(login_url='/login')
def checkout(request):
    currentuser = request.user
    shopcarts = ShopCart.objects.filter(user_id=currentuser.id)
    customer = Customer.objects.get(user_id=currentuser.id)
    myuser = User.objects.get(id=currentuser.id)

    total = 0
    qty = 0
    for shopcart in shopcarts:
        total = total + shopcart.amount
        qty = qty + shopcart.qty
    
    discount = 10/100 * total
    if discount > 20000:
        discount = 20000

    grand_total = total - discount

    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        house_no = request.POST['house_no']
        street = request.POST['street']
        state = request.POST['state']
        city = request.POST['city']
        pin = request.POST['pin']
        code = get_random_string(5).upper()

        order = Order(
            user_id = currentuser.id,
            first_name = firstname,
            last_name = lastname,
            phone = phone,
            house_no = house_no,
            street = street,
            city = city,
            pin = pin,
            state = state,
            total = grand_total
        )
        order.save()

        for shopcart in shopcarts:
            orderpr = OrderProduct(
                order_id = order.id,
                user_id = currentuser.id,
                product_id = shopcart.product_id,
                qty = shopcart.qty,
                price = shopcart.product.price,
                amount = shopcart.amount,
                total = grand_total
            )
            orderpr.save()
        
        ShopCart.objects.filter(user_id=currentuser.id).delete()
        messages.success(request, "Order has been placed. Thank You 😊")
        return redirect('ShopHome')
    
    details = {
        'myuser':myuser,
        'customer':customer,
        'shopcarts':shopcarts,
        'qty':qty,
        'total':total,
        'discount':discount,
        'grand_total':grand_total,
    }
    
    return render(request, 'checkout.html', details)