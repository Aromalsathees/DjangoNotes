from django.urls import path  
from .views import *


urlpatterns = [
    path('',home,name='home'),
    path('register_view/',register_view,name='register_view')

]