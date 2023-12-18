from django.shortcuts import render
from book.models import Book
from .models import Wishlist
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django.core import serializers
import json

# Create your views here.

# ========== Views for wishlist ==========
# search book by isbn
def search_book(request, isbn):
    # cek apakah ada di database
    # hapus huruf a pada isbn
    book = Book.objects.filter(isbn=isbn)
    book = book[0]
    temp = {
        'pk': book.pk,
        'title': book.title,
        'num_of_pages': str(book.num_of_pages),
        'language': book.language,
        'authors': book.authors,
        'publisher': book.publisher,
        'isbn': book.isbn,
        'image_url': book.image_url,
        'small_image_url': book.small_image_url,
        'publish_day': str(book.publish_day),
        'publish_month': str(book.publish_month),
        'publish_year': str(book.publish_year),
    }
    return HttpResponse(json.dumps(temp), content_type="application/json")


def show_whishlist(request):
    # Menampilkan wishlist by user
    wishlists = Wishlist.objects.filter(user=request.user)
    context = {
        'my_wishlist': wishlists
    }
    return render(request, 'wishlist.html', context)

def get_wishlist_json(request):
    # Mengambil semua object wishlist by user
    wishlist = Wishlist.objects.filter(user=request.user)
    books = [wish.book for wish in wishlist]
    return HttpResponse(serializers.serialize("json",books),content_type="application/json")

@login_required(login_url='/login/')
@csrf_exempt
def add_wishlist_flutter(request, book_id):
    if request.method == 'POST':
        # Ambil buku yang sesuai dengan book_id
        book = Book.objects.get(pk=book_id)
        user = request.user
        # Cek apakah buku sudah ada di wishlist
        if Wishlist.objects.filter(user=user, book=book).exists():
            # Kirim status bahwa data sudah ada
            return JsonResponse({"status": "existed"}, status=200)
        wishlist = Wishlist(user=user, book=book)
        wishlist.save()
        return JsonResponse({"status": "success"}, status=201)
    else:
        return JsonResponse({"status": "error"}, status=401)

# ---------- Views for CRUD ----------
def remove_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    user = request.user
    wishlist = Wishlist.objects.get(user=user, book=book)
    wishlist.delete()
    return HttpResponseRedirect('')

# get book object
def get_book_object(request, book_id):
    book = Book.objects.get(pk=book_id)
    # mengambil semua atribut buku dan mengubah non string menjadi string dengan str()
    temp = {
        'book_id': book.book_id,
        'title': book.title,
        'num_of_pages': book.num_of_pages,
        'language': book.language,
        'authors': book.authors,
        'publisher': book.publisher,
        'isbn': book.isbn,
        'counts_of_review': book.counts_of_review,
        'rating_dist_total': book.rating_dist_total,
        'rating': book.rating,
        'rating_dist1': book.rating_dist1,
        'rating_dist2': book.rating_dist2,
        'rating_dist3': book.rating_dist3,
        'rating_dist4': str(book.rating_dist4),
        'rating_dist5': book.rating_dist5,
        'indices': book.indices,
        'distance': book.distance,
        'image_url': book.image_url,
        'small_image_url': book.small_image_url,
        'publish_day': book.publish_day,
        'publish_month': book.publish_month,
        'publish_year': book.publish_year,
        'status': book.status,
        'return_date': book.return_date
    }
    return JsonResponse(temp)


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