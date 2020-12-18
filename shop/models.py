from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.forms import ModelForm
from django.utils.timezone import now


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="")
    phone = models.IntegerField()
    address = models.CharField(null=True, max_length=50, default="")
    profile_pic = models.ImageField(null=True, upload_to="customer_pic")

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=20)

    def __str__(self):
        return self.brand_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.CharField(max_length=20, default="")
    price = models.IntegerField(default=0)
    tag = models.CharField(default="New", max_length=10)
    product_img = models.ImageField(upload_to="shop/images", default="")
    product_img1 = models.ImageField(upload_to="shop/images", default="")
    product_img2 = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    qty = models.IntegerField()

    @property
    def price(self):
        return self.product.price

    @property
    def amount(self):
        return self.qty * self.product.price

    def __str__(self):
        return self.product.product_name + " by " + self.user.username


STATUS = (
    ('Placed', 'Placed'),
    ('Confirmed', 'Confirmed'),
    ('Preparing', 'Preparing'),
    ('Shipped', 'Shipped'),
    ('Out For Delivery', 'Out For Delivery'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone = models.IntegerField(null=True)
    house_no = models.CharField(null=True, max_length=20)
    street = models.CharField(null=True, max_length=50)
    city = models.CharField(null=True, max_length=20)
    pin = models.IntegerField(null=True)
    state = models.CharField(null=True, max_length=20)
    total = models.FloatField()
    code = models.CharField(max_length=6, default="")
    placed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    price = models.FloatField()
    amount = models.FloatField()
    total = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS, default='Placed')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.product_name + " by " + self.user.first_name

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    review = models.CharField(max_length=200)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.product_name + " by " + self.user.first_name


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.user.first_name + " - " + self.product.product_name