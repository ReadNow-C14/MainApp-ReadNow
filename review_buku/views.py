from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from book.models import Book
from review_buku.forms import ReviewForm
from review_buku.models import Review
from django.core import serializers
from django.shortcuts import redirect, render
from django.contrib import messages
import datetime

def reviews_for_book(request, book_id):
    book = Book.objects.get(id=book_id)
    reviews = Review.objects.filter(book=book)
    form = ReviewForm()
    return render(request, 'review_buku.html', {'reviews': reviews, 'book': book, 'form': form})

def review_json(request, product_id):
    data = Review.objects.all()
    return HttpResponse(serializers.serialize('json', data))

@login_required(login_url='/login/')
@csrf_exempt
def submit_review(request, book_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = Review.objects.get(user__id=request.user.id, book__id=book_id)
            form = ReviewForm(request.POST, instance=reviews)
        except Review.DoesNotExist:
            form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book_id = book_id
            review.save()
            messages.success(request, 'Thank you! Your review has been submitted.')
            return redirect(url)
        else:
            messages.error(request, 'There was an error with your submission.')
            return redirect(url)
