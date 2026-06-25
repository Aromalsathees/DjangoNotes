from django.urls import path  
from .views import *


urlpatterns = [
    
    path('',home,name='home'),
    path('profile/',profile,name='view_profile'),
    path('register_view/',register_view,name='register_view'),
    path('login_view/',Login,name='login')

]