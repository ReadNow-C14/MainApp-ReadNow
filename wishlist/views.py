from django.shortcuts import render
from book.models import Book
from .models import Wishlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_whishlist(request):
    # Menampilkan wishlist
    wishlists = Wishlist.objects.filter(user=request.user)
    context = {
        'my_wishlist': wishlists
    }
    return render(request, 'wishlist.html', context)

def get_wishlist_json(request):
    # TODO: buat filter berdasarkan user, karena saat ini ambil semua objek buku
    # Mengambil semua object buku
    wishlist = Wishlist.objects.all()
    return HttpResponse(serializers.serialize("json",wishlist),content_type="application/json")

def add_wish(request, id):
    # Menambahkan buku ke wishlist
    book = Book.objects.get(pk=id)
    Wishlist.objects.create(user=request.user, book=book)
    return render(request, 'wishlist.html')

def delete_wish(request, id):
    # Menghapus buku dari wishlist
    book = Book.objects.get(pk=id)
    Wishlist.objects.get(user=request.user, book=book).delete()
    return render(request, 'wishlist.html')


def show_books(request):
    # Menampilkan semua buku
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'utama.html', context)