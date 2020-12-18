from django.urls import path, include
from .views import index, signup, login, productdetail, products, addtocart, buynow, checkout, logout, cart, account, deletefromcart
from .views import addtowishlist, removefromwishlist, search, updateprofile, changepassword, postreview, contact, about
from django.conf import settings

urlpatterns = [
    path("", index.index, name="ShopHome"),
    path("signup/", signup.Signup.as_view(), name="SignUp"),
    path("login/", login.Login.as_view(), name="LogIn"),
    path("products/", products.products, name="Products"),
    path("search/", search.search, name="Search"),
    path("productdetail/<int:prid>", productdetail.productdetail, name="ProductDetail"),
    path("addtocart/<int:prid>", addtocart.addtocart, name="AddtoCart"),
    path("buynow/<int:prid>", buynow.buynow, name="BuyNow"),
    path("postreview/<int:prid>", postreview.postreview, name="PostReview"),
    path("deletefromcart/<int:prid>", deletefromcart.deletefromcart, name="DeletefromCart"),
    path("addtowishlist/<int:prid>", addtowishlist.addtowishlist, name="AddfromWishlist"),
    path("removefromwishlist/<int:prid>", removefromwishlist.removefromwishlist, name="RemovefromWishlist"),
    path("cart/", cart.cart, name="Cart"),
    path("clearcart/", deletefromcart.clearcart, name="Cart"),
    path("checkout/", checkout.checkout, name="CheckOut"),
    path("contactus/", contact.contact, name="ContactUs"),
    path("about/", about.about, name="AboutUs"),
    path("account/", account.account, name="Account"),
    path("account/updateprofile/", updateprofile.updateprofile, name="UpdateProfile"),
    path("account/changepassword/", changepassword.changepassword, name="ChangePassword"),
    path("logout/", logout.logout_view, name="Logout")
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns