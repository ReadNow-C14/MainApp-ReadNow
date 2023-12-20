from django.urls import path
from .views import *

app_name = 'pinjam_buku'

urlpatterns = [
    path('get-borrowed-book/', get_borrowed_book_json, name='get_borrowed_book_json'),
    path('get-borrowed-bookk/', get_borrowed_book_jsonn, name='get_borrowed_book_jsonn'),
    path('borrow-book-ajax/<int:id>', borrow_book_ajax, name='borrow_book_ajax'),
    path('borrowed-books/', borrowed_books, name='borrowed_books'),

    path('return-book-ajax/<int:id>', return_book_ajax, name='return_book_ajax'),
    path('return-book-flutter/<int:id>/', return_book_flutter, name='return_book_flutter'),
    
    path('borrow-flutter/<int:book_id>/', borrow_flutter, name='borrow_flutter'),
    path('borroww_book_flutter/', borroww_book_flutter, name='borroww_book_flutter'),
    path('borrow-book-flutter/<int:book_id>/', borrow_book_flutter, name='borrow_book_flutter'),
    path('borrow-book-flutteer/<int:book_id>/', borrow_book_flutteer, name='borrow_book_flutteer'),
    path('borrow-book-flutteeer/<int:book_id>/', borrow_book_flutteeer, name='borrow_book_flutteeer'),
]