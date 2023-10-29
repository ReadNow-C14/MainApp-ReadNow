from django.shortcuts import render, get_object_or_404
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from pinjam_buku.forms import BorrowForm, BorrowedBook
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Book
from django.http import JsonResponse

# Create your views here.

@login_required(login_url='/login')
def borrowed_books(request):
    borrowed_books = BorrowedBook.objects.filter(user=request.user)
    total_borrowed_books = borrowed_books.count()

    context = {
        'name': request.user.username,
        'total_borrowed_books' : total_borrowed_books,
        'borrowed_books' : borrowed_books,
    }
    return render(request, "borrowed_books.html", context)

@login_required(login_url='/login')
def get_borrowed_book_json(request):
    borrowed_books = BorrowedBook.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', borrowed_books))

@csrf_exempt
def borrow_book_ajax(request, id):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=id)
        return_date = request.POST.get("return_date")
        user = request.user
        book.status = "Borrowed"
        book.return_date = return_date
        book.save()

        new_borrowed_book = BorrowedBook(user=user, book=book, return_date=return_date)
        new_borrowed_book.save()

        return HttpResponse(b"BORROWED", status=201)

    return HttpResponseNotFound()

def return_book_ajax(request, id):
    borrowed_book = BorrowedBook.objects.get(pk=id)
    borrowed_book.delete()
    response = HttpResponseRedirect(reverse("pinjam_buku:borrowed_books"))
    return response