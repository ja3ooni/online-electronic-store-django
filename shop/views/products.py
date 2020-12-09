from django.shortcuts import render
from shop.models import Brand, Category, Product, ShopCart

def products(request):
    categories = Category.objects.all()

    categoryid = 0
    filtered_category = []

    try:
        categoryid = request.GET['category']
    except:
        pass

    if categoryid:
        products = Product.objects.filter(category_id=categoryid)
        filtered_category = Category.objects.get(id=categoryid)
    else:
        products = Product.objects.all()
    
    n = len(products)

    current_user = request.user
    carts = ShopCart.objects.filter(user_id=current_user.id)
    qty = 0
    for cart in carts:
        qty = qty + cart.qty

    params = {
        'products': products,
        'categories': categories,
        'filtered_category': filtered_category,
        'n': n,
        'qty': qty,
        }
    
    return render(request, 'products.html', params)