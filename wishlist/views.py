from django.shortcuts import render
from book.models import Book
from .models import Wishlist
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django.core import serializers

# Create your views here.

# ========== Views for wishlist ==========
def show_whishlist(request):
    # Menampilkan wishlist
    wishlists = Wishlist.objects.all()
    context = {
        'my_wishlist': wishlists
    }
    return render(request, 'wishlist.html', context)

def get_wishlist_json(request):
    # TODO: buat filter berdasarkan user, karena saat ini ambil semua objek buku
    # Mengambil semua object wishlist
    wishlist = Wishlist.objects.all()
    books = [wish.book for wish in wishlist]
    return HttpResponse(serializers.serialize("json",books),content_type="application/json")
# ---------- Views for CRUD ----------
def remove_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    user = request.user
    wishlist = Wishlist.objects.get(user=user, book=book)
    wishlist.delete()
    return HttpResponseRedirect('')


# ========== Views for books ==========
def show_books(request):
    # ambil semua objek buku
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books.html', context)

def get_books_json(request):
    # Mengambil semua object buku
    books = Book.objects.all()
    return HttpResponse(serializers.serialize("json",books),content_type="application/json")
# ---------- Views for CRUD ----------
def add_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    user = request.user
    # cek apakah buku sudah ada di wishlist
    if Wishlist.objects.filter(user=user, book=book).exists():
        return HttpResponseRedirect('')
    wishlist = Wishlist(user=user, book=book)
    wishlist.save()
    return HttpResponseRedirect('')