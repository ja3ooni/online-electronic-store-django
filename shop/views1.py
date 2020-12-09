from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import Customer, Product

def index(request):
    products = Product.objects.all()
    print(products)
    params = {'products': products}
    return render(request, 'shop/index.html', params)

def signup(request):
    if request.method == 'GET':
        return render(request, 'shop/signup.html')

    else:
        postData = request.POST
        fname = postData.get('fname')
        lname = postData.get('lname')
        email = postData.get('email')
        phone = postData.get('phone')
        dob = postData.get('dob')
        pass1 = postData.get('pass1')
        pass2 = postData.get('pass2')
        print(fname, lname, email, phone, dob, pass1)

        value = {
            'first_name': fname,
            'last_name': lname,
            'email': email,
            'phone': phone,
            'dob': dob
        }

        error_msg = None
        # Form Validations
        if len(fname)>10 and len(lname)>10:
            error_msg = "First or Last Name too long!!!"
        if not fname.isalpha() or not lname.isalpha():
            error_msg = "Name must contain only letters."
        if len(str(phone))!=10:
            error_msg = "Phone number must contain 10 digits."
        if len(pass1)<5:
            error_msg = "Password too short. It must have atleast 5 characters."
        if pass1!=pass2:
            error_msg = "Passwords don't match!!!"

        customer = Customer (
                first_name = fname,
                last_name = lname,
                email = email,
                phone = phone,
                dob = dob,
                password = pass1
            )
        
        if customer.isEmailExists():
            error_msg = "E-mail Already Exists."
        
        if not error_msg:
            customer.password = make_password(customer.password)
            customer.save()
            return redirect('ShopHome')

        else:
            data = {
                'error' : error_msg,
                'values' : value
            }
            return render(request, 'shop/signup.html', data)

def login(request):
    if request.method == 'GET':
        return render(request, 'shop/login.html')
    else:
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        customer = Customer.getCustomer(email)
        error_msg = None
        if customer:
            flag = check_password(pass1, customer.password)
            if flag:
                return redirect('ShopHome')
            else:
                error_msg = "Invalid E-mail or Password!!!"
        else:
            error_msg = "Invalid E-mail or Password!!!"
        return render(request, 'shop/login.html', {'error':error_msg})

def search(request):
    return HttpResponse("we are at search")

def product(request, myid):
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, 'shop/product.html', {'product':product[0]})

def checkout(request):
    return render(request, 'shop/checkout.html')

def tracker(request):
    return HttpResponse("we are at tracker")

def contact(request):
    return render(request, 'shop/contactus.html')

def about(request):
    return render(request, 'shop/about.html')