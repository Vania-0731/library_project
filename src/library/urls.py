# urls.py
from django.urls import path
from . import views
from .api_views import (
    HomeStatsAPI, AuthorListAPI, AuthorDetailAPI,
    BookListAPI, BookDetailAPI, CategoryListAPI, CategoryDetailAPI,
)

urlpatterns = [
    # 🌐 HTML template views
    path('', views.home, name='home'),  # 🏠 Home page
    path('authors/', views.author_list, name='author_list'),  # 👨‍🎨 Authors list
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),  # 👨‍🎨 Author detail
    path('books/', views.book_list, name='book_list'),  # 📚 Books list
    path('books/<int:pk>/', views.book_detail, name='book_detail'),  # 📖 Book detail
    path('categories/', views.category_list, name='category_list'),  # 🏷️ Categories list
    path('categories/<slug:slug>/', views.category_detail, name='category_detail'),  # 🏷️ Category detail

    # 🔌 API endpoints (Django REST Framework views)
    path('api/home/', HomeStatsAPI.as_view(), name='api_home'),
    path('api/authors/', AuthorListAPI.as_view(), name='api_author_list'),
    path('api/authors/<int:pk>/', AuthorDetailAPI.as_view(), name='api_author_detail'),
    path('api/books/', BookListAPI.as_view(), name='api_book_list'),
    path('api/books/<int:pk>/', BookDetailAPI.as_view(), name='api_book_detail'),
    path('api/categories/', CategoryListAPI.as_view(), name='api_category_list'),
    path('api/categories/<slug:slug>/', CategoryDetailAPI.as_view(), name='api_category_detail'),
]
