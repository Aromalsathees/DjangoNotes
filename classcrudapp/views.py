from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import *
from django.urls import reverse_lazy
# Create your views here.

# Data listing
class BookListView(ListView):
    model = Book
    template_name = 'authentication/book_list.html '
    context_object_name = 'books'

# data creating
class BookCreateView(CreateView):
    model = Book 
    fields = ['title','author','desc','image']
    template_name = 'authentication/book_form.html'
    success_url = reverse_lazy('booklist')

# view Book details
class BookDetailView(DetailView):
    model = Book 
    template_name = 'authentication/book_detail.html'
    context_object_name = 'book'

# delete a book details
class BookDeleteview(DeleteView):
    model = Book 
    template_name = 'authentication/book_confirm_delete.html'
    success_url = reverse_lazy('booklist')

# update a book
class BookUpdateview(UpdateView):
    model = Book 
    fields = ['title','author','desc','image']
    template_name = 'authentication/book_form.html'
    success_url = reverse_lazy('book_list')