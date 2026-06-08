from django.shortcuts import render,redirect
from products.models import Add_Products


def about(request):
    return render(request,'about.html')

def home(request):
    # data is created to backend from here
    if request.method == 'POST':
        get_name = request.POST.get('name')
        get_descriptio = request.POST.get('descrition')
        get_price = request.POST.get('price')

        # print(get_name,get_descriptio,get_price)

        add_product = Add_Products(
            product_name=get_name,
            product_desc=get_descriptio,
            product_price=get_price
        )
        add_product.save()
        redirect('home_url')
   # data is created to backend from here


# data is fetched from database
    products = Add_Products.objects.all()
    context = {
        'products':products,
    }
    # data is fetched from database

    return render(request,'home.html',context)


def delete_product(request,id):
    print(id)
    get_data = Add_Products.objects.get(id=id)
    print(get_data)
    get_data.delete()
    print(get_data)
    return redirect('home_url')


def payment(request):
    return render(request,'payment.html')


def update_product(request,id):
    
    get_data = Add_Products.objects.get(id=id)

    if request.method == 'POST':
        get_data.product_name = request.POST.get('name')
        get_data.product_desc = request.POST.get('descrition')
        get_data.product_price = request.POST.get('price')

        get_data.save()
        return redirect('home_url')

            


    context = {
        'get_data':get_data
    }
    return render(request,'update.html',context)





