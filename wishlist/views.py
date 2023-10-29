from django.shortcuts import render
from book.models import Book
from .models import Wishlist
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotFound
from django.core import serializers

# Create your views here.
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

def add_wish(request, id):
    # Menambahkan buku ke wishlist
    book = Book.objects.get(pk=id)
    # cek apakah buku sudah ada di wishlist
    if Wishlist.objects.filter(user=request.user, book=book).exists():
        # jika sudah ada, maka tidak perlu ditambahkan lagi
        pass
    else:
        # jika belum ada, maka tambahkan
        Wishlist.objects.create(user=request.user, book=book)
    return HttpResponseRedirect('/')

def delete_wish(request, id):
    # Menghapus buku dari wishlist
    book = Book.objects.get(pk=id)
    Wishlist.objects.get(user=request.user, book=book).delete()
    return HttpResponseRedirect('/')

def add_wish_ajax(request):
    if request.method == 'POST':
        book = request.post.get('book')
        user = request.user
        new_wish = Wishlist(user=user, book=book)
        new_wish.save()
        return JsonResponse({'message': 'Item added to wishlist'}, status=201)
    return HttpResponseNotFound()

def delete_wish_ajax(request, id):
    try:
        # ambil objek wishlist yang akan dihapus
        book = Book.objects.get(pk=id)
        wishlist = Wishlist.objects.get(user=request.user, book=book)
        # hapus wishlist
        wishlist.delete()
        return HttpResponseRedirect('/wishlist/')
    except Wishlist.DoesNotExist:
        return JsonResponse({'message': 'Item does not exist in wishlist'}, status=404)

def get_books_json(request):
    # Mengambil semua object buku
    books = Book.objects.all()
    return HttpResponse(serializers.serialize("json",books),content_type="application/json")