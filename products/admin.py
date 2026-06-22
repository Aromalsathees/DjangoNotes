from django.contrib import admin
from .models import Add_Products, Category
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','product_desc','product_price','category')

class CatgeoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','created_at')

admin.site.register(Add_Products,ProductAdmin)
admin.site.register(Category,CatgeoryAdmin)

