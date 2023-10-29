from django.urls import path
from .views import *

app_name = 'wishlist'

urlpatterns = [
    # CRUD
    path('add-book/<int:book_id>/', add_book, name='add_book'),
    path('remove-book/<int:book_id>/', remove_book, name='remove_book'),
    path('get-book-object/<int:book_id>/', get_book_object, name='get_book_object'),
    # wishlist
    path('search-book/<str:isbn>', search_book, name='search_book'),
    path('get-wishlist/', get_wishlist_json, name='get_wishlist_json'),
    path('my-wishlist/', show_whishlist, name='show_whishlist'),
    # book list
    path('get-books/', get_books_json, name='get_books_json'),
    path('', show_books, name='show_books'),
]