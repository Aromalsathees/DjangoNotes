from django.contrib import admin
from .models import Book
# Register your models here.


class crudAdmin(admin.ModelAdmin):
    list_display = ['title','author','desc']


admin.site.register(Book,crudAdmin)