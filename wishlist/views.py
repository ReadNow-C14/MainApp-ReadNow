from django.shortcuts import render
from book.models import Book

# Create your views here.
def show_wishlist(request):
    context = {
        'books': Book.objects.all(),
    }
    return render(request, 'wishlist.html', context)