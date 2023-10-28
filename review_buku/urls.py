from django.urls import path
from review_buku.views import *

urlpatterns = [
    path('<int:book_id>/', reviews_for_book, name='reviews_for_book'),
    path('submit_review/<int:book_id>/', submit_review, name='submit_review'),
    path('review_json/', review_json, name='review_json'),
]
