from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from book.models import Book
from review_buku.forms import ReviewForm
from review_buku.models import Review
from django.core import serializers
from django.shortcuts import redirect, render
from django.contrib import messages
import datetime
from django.http import JsonResponse

def reviews_for_book(request, book_id):
    book = Book.objects.get(id=book_id)
    reviews = Review.objects.filter(book=book)
    form = ReviewForm()
    return render(request, 'review_buku.html', {'reviews': reviews, 'book': book, 'form': form})

def review_json(request, book_id):
    book = Book.objects.get(id=book_id)
    data = Review.objects.filter(book=book)
    return HttpResponse(serializers.serialize('json', data))

@login_required(login_url='/login/')
@csrf_exempt
def submit_review(request):
    if request.method == 'POST':
        book = request.POST.get('book')
        user = request.user
        comment = request.POST.get('comment')
        new_rev = Review(user=user, book=book, comment=comment)
        new_rev.save()
        return JsonResponse({'message': 'Review Added!'}, status=201)
    return HttpResponseNotFound()
    

