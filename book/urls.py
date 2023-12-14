from django.urls import path, include
from book.views import *

app_name = "book"

urlpatterns = [
    path("",get_books, name="get_books"),
    path("by-isbn/<str:isbn>",get_book_by_isbn, name="get_book_by_isbn"),
]