from django.contrib import admin
from .models import Add_Products
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','product_desc','product_price')

admin.site.register(Add_Products,ProductAdmin)

