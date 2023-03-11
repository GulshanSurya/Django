from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order

class AdminProduct(admin.ModelAdmin):           #this makes the record in the db shown by name instead as product object
    list_display = ['name', 'price', 'category']
    
class AdminCategory(admin.ModelAdmin):     #this makes the record in the db shown by name instead as product object
    list_display= ['name']
    
class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'email'] 

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)