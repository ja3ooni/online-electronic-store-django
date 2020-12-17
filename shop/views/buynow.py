from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from shop.models import ShopCart

@login_required(login_url='/login')
def buynow(request, prid):
    current_user = request.user
    ShopCart.objects.filter(user_id=current_user.id).delete()
    data = ShopCart()
    data.user_id = current_user.id
    data.product_id = prid
    data.qty = 1
    data.save()
    return HttpResponseRedirect('/cart')