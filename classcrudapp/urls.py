from django.urls import path  
from .views import *


urlpatterns = [

    path('',BookListView.as_view(), name='booklist'),
    path('book_create/',BookCreateView.as_view(),name='book_create'),
    path('book_detail/<int:pk>/',BookDetailView.as_view(),name='book_detail'),
    path('book_delete/<int:pk>/',BookDeleteview.as_view(),name='book_delete'),
    path('book_update/<int:pk>/',BookUpdateview.as_view(),name='book_update'),

]