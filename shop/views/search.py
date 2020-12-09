from django.shortcuts import render
from shop.models import Brand, Category, Product, ShopCart


def searchMatch(search, prod):
    if search.lower() in prod.description.lower() or search in prod.product_name.lower() or search in prod.category.category_name.lower():
        return True
    else:
        return False

def checkCategory(categoryid, prod):
    if prod.category_id == int(categoryid):
        return True
    else:
        return False

def search(request):
    search = request.GET['search']
    products = []
    categoryid = 0

    try:
        categoryid = request.GET['category']
    except:
        pass

    allproducts = Product.objects.all()
    categories = Category.objects.all()

    for products in allproducts:
        if categoryid:
            products = [prod for prod in allproducts if searchMatch(search, prod) and checkCategory(categoryid, prod)]
        else:
            products = [prod for prod in allproducts if searchMatch(search, prod)]

    n = len(products)

    current_user = request.user
    carts = ShopCart.objects.filter(user_id=current_user.id)
    qty = 0
    for cart in carts:
        qty = qty + cart.qty

    params = {
        'products': products,
        'n': n,
        'search': search.lower(),
        'categories': categories,
        'qty': qty
        }
    return render(request, 'search.html', params)
