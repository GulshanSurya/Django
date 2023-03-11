from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View


# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')               #.post bolne se ek dictionary milega ans get se ek specific product
        remove = request.POST.get('remove')                 #quantity remove krne m kam aaegaa "remove is name defined in index.html"
        cart = request.session.get('cart')                  #session ek dictionary hai and session se hum cart ko access krenge
        if cart:                                            #if cart exists phle se hi then product ko append krna hai
            quantity = cart.get(product)
            if quantity:
                if remove:                                  #if remove input aaya from cart
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:                                            #if cart doesn't exist we will create a new
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart                   #ab jo bhi hai usko session m add kr do
        print('cart' , request.session['cart'])
        return redirect('homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products();

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)

