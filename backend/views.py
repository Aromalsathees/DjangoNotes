from django.shortcuts import render,redirect
from products.models import Add_Products
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

def register(request):

    if request.method == 'POST':
    
        # geting the payload 
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('cpassword')
        
        # checking whetere the credentials are ok or not
        if password != confirm_password:
            messages.error(request,'password do not match')

        if User.objects.filter(username=username).exists():
            messages.error(request,'username already exist')

        if User.objects.filter(email=email).exists():
            messages.error(request,'email id already exist')
        
        # saving data to database
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password    
        )
        user.save()

        messages.success(request,'you are succesfully registerd your account')
        return redirect('login')

    return render(request,'authentication/register.html')


def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)
            messages.success(request,'welcome back')
            return redirect('home')
        else:
            messages.error(request,'invalid credentials')
            return redirect('login')

    return render(request,'authentication/login.html')

@login_required(login_url='login')
def home(request):
    return render(request,'authentication/home.html')















# def about(request):
#     return render(request,'about.html')

# def home(request):
#     # data is created to backend from here
#     if request.method == 'POST':
#         get_name = request.POST.get('name')
#         get_descriptio = request.POST.get('descrition')
#         get_price = request.POST.get('price')

#         # print(get_name,get_descriptio,get_price)
   

#         add_product = Add_Products(
#             product_name=get_name,
#             product_desc=get_descriptio,
#             product_price=get_price
#         )
#         add_product.save()
#         redirect('home_url')
#    # data is created to backend from here


# # data is fetched from database
#     products = Add_Products.objects.all()
#     context = {
#         'products':products,
#     }
#     # data is fetched from database

#     return render(request,'home.html',context)


# def delete_product(request,id):
#     print(id)
#     get_data = Add_Products.objects.get(id=id)
#     print(get_data)
#     get_data.delete()
#     print(get_data)
#     return redirect('home_url')


# def payment(request):
#     return render(request,'payment.html')


# def update_product(request,id):
    
#     get_data = Add_Products.objects.get(id=id)

#     if request.method == 'POST':
#         get_data.product_name = request.POST.get('name')
#         get_data.product_desc = request.POST.get('descrition')
#         get_data.product_price = request.POST.get('price')

#         get_data.save()
#         return redirect('home_url')

            


#     context = {
#         'get_data':get_data
#     }
#     return render(request,'update.html',context)





