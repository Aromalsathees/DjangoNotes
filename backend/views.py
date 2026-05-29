from django.shortcuts import render
from products.models import Add_Products

def home(request):
    products = Add_Products.objects.all()
    context = {
        'products':products
    }
    return render(request,'home.html',context)