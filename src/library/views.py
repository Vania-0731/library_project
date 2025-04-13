from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Author, Book, Category, Publisher

def home(request):
    return render(request, 'library/home.html')

def author_list(request):
    return render(request, 'library/author_list.html')

def author_detail(request, pk):
    return render(request, 'library/author_detail.html', {'author_id':pk})

def book_list(request): 
    return render(request, 'library/book_list.html')

def book_detail(request, pk):
    
    return render(request, 'library/book_detail.html')

def category_list(request):
    return render(request, 'library/category_list.html')

def category_detail(request, slug):
    return render(request, 'library/category_detail.html', {'slug' : slug})
