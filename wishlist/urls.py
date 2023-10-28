from django.urls import path
from .views import *

app_name = 'wishlist'

urlpatterns = [
    path('utama/', show_books, name='show_books'),
    path('add-wish/<int:id>/', add_wish, name='add_wish'),
    path('delete-wish/<int:id>/', delete_wish, name='delete_wish'),
    path('get-wishlist/', get_wishlist_json, name='get_wishlist_json'),
    path('', show_whishlist, name='show_whishlist'),
]