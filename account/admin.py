from django.contrib import admin
from .models import *
# Register your models here.

class CustomUserModel(admin.ModelAdmin):
    list_display = ['username','email','password']


admin.site.register(CustomUser,CustomUserModel)

admin.site.register(Profile)