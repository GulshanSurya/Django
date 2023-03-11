from django.db import models
from django.core.validators import MinLengthValidator


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    
    def register(self):                   #register krne k liye
        self.save()
        
    @staticmethod
    def get_customer_by_email(email):          #Get method se single result/object milta hai. Get jb aapne use kiya to ya to aapko result milega ya fir error milega. If you want not to mess with it simply use filter. Isliye humne try and except use kiya hai customers.py me
        try:
            return Customer.objects.get(email=email)  #filter changed to get
        except:
            return False
        
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        
        else:
            return False