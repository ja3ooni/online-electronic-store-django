from django.contrib.auth.decorators import login_required
from django.contrib import messages
from shop.models import ShopCart
from django.http.response import HttpResponseRedirect

@login_required(login_url='/login')
def addtocart(request, prid):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    check_product = ShopCart.objects.filter(user_id=current_user.id, product_id=prid)
        
    if check_product:
        control = 1
    else:
        control = 0
    
    if control == 1:
        data = ShopCart.objects.get(user_id=current_user.id, product_id=prid)
        data.qty = data.qty + 1
        data.save()
    else:
        data = ShopCart()
        data.user_id = current_user.id
        data.product_id = prid
        data.qty = 1
        data.save()
    messages.success(request, data.product.product_name + " added to the Cart.")
    return HttpResponseRedirect(url)