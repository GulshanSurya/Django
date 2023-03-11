from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')       #post ek dictionary hai jismeki humne key pass ki hai i.e address
        phone = request.POST.get('phone')
        customer = request.session.get('customer')    #customer ka id milega login hai jo
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))  #product ka price laenge db se
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}    #order ho jaega confirm tb cart ko khali kr denge, cart replace ho jaega ek empty dictionary se

        return redirect('cart')