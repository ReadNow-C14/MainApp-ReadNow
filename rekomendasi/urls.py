from django.urls import path
from rekomendasi.views import *

app_name = 'rekomendasi'

urlpatterns = [
    path('similar-books/<int:id>', similar_books, name='similar_books'),
    path('json/', get_recommendations_json, name='get_recommendations_json'),
    path('filter-books-ajax/<int:id>', filter_books_ajax, name='filter_books_ajax'),
    path('isbn-search/',isbn_search,name="isbn_search")
]