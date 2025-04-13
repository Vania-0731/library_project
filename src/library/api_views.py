# api_views.py
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from .models import Author, Book, Category, Publisher
from .serializers import (
    AuthorSerializer, BookSerializer, CategorySerializer
)


class HomeStatsAPI(APIView):
    def get(self, request):
        data = {
            'total_books': Book.objects.count(),
            'total_authors': Author.objects.count(),
            'total_categories': Category.objects.count(),
            'total_publishers': Publisher.objects.count(), 
            'categories': CategorySerializer(
                Category.objects.annotate(book_count=Count('books')).order_by('-book_count')[:5],
                many=True
            ).data,
            'recent_books': BookSerializer(
                Book.objects.select_related('author').prefetch_related('categories').order_by('-publication_date')[:5],
                many=True
            ).data
        }
        return Response(data)


class AuthorListAPI(APIView):
    def get(self, request):
        authors = Author.objects.all().order_by('name')
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)


class AuthorDetailAPI(APIView):
    def get(self, request, pk):
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)


class BookListAPI(APIView):
    def get(self, request):
        books = Book.objects.select_related('author').prefetch_related('categories')
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class BookDetailAPI(APIView):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
class CategoryListAPI(APIView):
    def get(self, request):
        categories = Category.objects.annotate(book_count=Count('books')).order_by('name')
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CategoryDetailAPI(APIView):
    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        books = category.books.select_related('author').all()
        book_serializer = BookSerializer(books, many=True)
        category_serializer = CategorySerializer(category)
        return Response({
            'category': category_serializer.data,
            'books': book_serializer.data
        })
