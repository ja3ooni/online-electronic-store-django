from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from shop.models import ShopCart
from django.http.response import HttpResponseRedirect

def deletefromcart(request, prid):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    product = ShopCart.objects.get(user_id=current_user.id, product_id=prid)
        
    if product.qty == 1:
        product.delete()
    else:
        product.qty = product.qty - 1
        product.save()
    
    messages.success(request, product.product.product_name + " deleted from the Cart.")
    return HttpResponseRedirect(url)

def clearcart(request):
    current_user = request.user
    ShopCart.objects.filter(user_id=current_user.id).delete()
    return HttpResponseRedirect('/cart')