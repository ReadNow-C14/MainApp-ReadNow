from django.urls import path
from review_buku.views import *

urlpatterns = [
    path('<int:book_id>/', reviews_for_book, name='reviews_for_book'),
    path('submit_review/<int:book_id>/', submit_review, name='submit_review'),
    path('review_json/', review_json, name='review_json'),
    path('submit-review-ajax/<int:book_id>',submit_review_ajax,name='submit_review_ajax'),
    path('get-review-json/<int:book_id>',get_review_json,name='get_review_json'),
    path('submit-review-flutter/<int:book_id>',submit_review_flutter,name='submit_review_flutter')
]
