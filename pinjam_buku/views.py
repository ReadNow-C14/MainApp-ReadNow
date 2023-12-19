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
import json

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
    books = [borrowed.book for borrowed in borrowed_books]
    return HttpResponse(serializers.serialize("json",books),content_type="application/json")

def get_borrowed_book_jsonn(request):
    borrowed_books = BorrowedBook.objects.all()
    books = [borrowed for borrowed in borrowed_books]
    return HttpResponse(serializers.serialize("json",books),content_type="application/json")

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

@csrf_exempt
def return_book_ajax(request, id):
    borrowed_book = BorrowedBook.objects.filter(user=request.user)
    for book in borrowed_book:
        if book.book.id == id:
            book.book.status = "Available"
            book.book.save()
            book.delete()
    return HttpResponse(b"RETURNED", status=201)

@login_required(login_url='/login')
@csrf_exempt
def borrow_book_flutter(request, id):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        book = get_object_or_404(Book, pk=id)
        return_date = data["return_date"]

        book.status = "Borrowed"
        book.return_date = return_date
        book.save()

        new_borrowed_book = BorrowedBook.objects.create(
            user = request.user,
            book = book,
            return_date = return_date,
        )

        new_borrowed_book.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)