from django.urls import path  
from .views import create_order, verfiy_payment

urlpatterns = [
    path('order/',create_order),
    path('verify/',verfiy_payment)
]