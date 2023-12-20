from django.urls import path
from .views import *

app_name = 'pinjam_buku'

urlpatterns = [
    path('get-borrowed-book/', get_borrowed_book_json, name='get_borrowed_book_json'),
    path('get-borrowed-bookk/', get_borrowed_book_jsonn, name='get_borrowed_book_jsonn'),
    path('borrow-book-ajax/<int:id>', borrow_book_ajax, name='borrow_book_ajax'),
    path('borrowed-books/', borrowed_books, name='borrowed_books'),
    path('return-book-ajax/<int:id>', return_book_ajax, name='return_book_ajax'),
    path('borrow-book-flutter/<int:book_id>/', borrow_book_flutter, name='borrow_book_flutter'),
    path('return-borrowed-book-flutter/<int:book_id>/', return_borrowed_book_flutter, name='return_borrowed_book_flutter'),
    path('borrow-flutter/<int:book_id>/', borrow_flutter, name='borrow_flutter'),
    path('add-wishlist-flutterr/<int:book_id>/', add_wishlist_flutterr, name='add_wishlist_flutterr'),
]