from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):                                                                  #sara order bill generate krrhe
    product = models.ForeignKey(Product, on_delete=models.CASCADE)                          #product hume create krna hai/krrhe hai
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)                                             #status checking whether the order is completed or not

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')         #-date means reverse order
