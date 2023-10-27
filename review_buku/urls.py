from django.urls import path
from review_buku.views import *

urlpatterns = [
    path('', show_review, name='show_forum'),
    path('add_review/', add_review_ajax, name='add_review'),
    path('review_json/', review_json, name='review_json'),
]
