"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from .views import register,login_view,home,logout_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [


    path('admin/', admin.site.urls),

    
    path('',include('account.urls')),
    path('products/',include('products.urls')),
    path('classcrudapp/',include('classcrudapp.urls')),


    #  DJANGO BASIC AUTHETICATION URLS STARTS HERE #######################################################################

    # path('',home,name='home'),
    # path('register_view/',register,name='register'),
    # path('login/',login_view,name='login'),
    # path('logout/',logout_view,name='logout'),

    #  DJANGO BASIC AUTHETICATION URLS ENDS HERE ###################################################################

   
    #  DJANGO BASIC CRUD URLS STARTS HERE ###################################################################

    # path('',home,name='home_url'), 
    # path('delete_product/<int:id>/',delete_product,name='delete_product'),
    # path('update_product/<int:id>/',update_product,name='update_product'),
    # path('about/',about),

    #  DJANGO BASIC CRUD URLS ENDS HERE ###################################################################
 
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
