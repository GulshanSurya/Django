from django.shortcuts import render , redirect , HttpResponseRedirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View


class Login(View):                                          #subclass of view class
    return_url = None
    def get(self , request):                                #if the request/method is GET
        Login.return_url = request.GET.get('return_url')
        return render(request , 'login.html')

    def post(self , request):                             #if the request/method is POST  #authentication part
        email = request.POST.get('email')                   #getting email from input-login form
        password = request.POST.get('password')             #getting password from input-login form
        customer = Customer.get_customer_by_email(email)    #getting customer from db
        error_message = None
        if customer:
            flag = check_password(password, customer.password)      #password = input-password from login-from, customer.password is password imported from db
            if flag:
                request.session['customer_id'] = customer.id           #is se hume ek dictionary milegi
                request.session['email'] = customer.email

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:                                                    
                    Login.return_url = None
                    return redirect('homepage')
            else:                                                       #if no user exist with the input email id then throw an error message
                error_message = 'Email or Password invalid !!'
        else:                                                           #if no user exist with the input email id then throw an error message
            error_message = 'Email or Password invalid !!'

        print(email, password)
        return render(request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')             #login page serve ho jaega, urls of Eshop

''' firstly we'll check whether it is a post method or get method 
'''