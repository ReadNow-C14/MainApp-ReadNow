from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from book.models import Book
from django.contrib.auth.models import User
from review_buku.forms import ReviewForm
from review_buku.models import Review
from django.core import serializers
from django.shortcuts import redirect, render
from django.contrib import messages
from datetime import datetime

def reviews_for_book(request, book_id):
    book = Book.objects.get(id=book_id)
    reviews = Review.objects.filter(book=book)
    form = ReviewForm()
    return render(request, 'review_buku.html', {'reviews': reviews, 'book': book, 'form': form})

def review_json(request):
    data = Review.objects.all()
    return HttpResponse(serializers.serialize('json', data))

def user_json(request):
    data = User.objects.all()
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
            return redirect(url)
        else:
            return redirect(url)
        
@login_required(login_url='/login/')
@csrf_exempt
def submit_review_ajax(request, book_id):
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
            
            return HttpResponse(b"CREATED", status=201)
        else:
            messages.error(request, 'There was an error with your submission.')
            return HttpResponseNotFound()
        
def get_review_json(request, book_id):
    book = Book.objects.get(pk = book_id)
    data_review = Review.objects.filter(book=book)
    data = [{'id_buk_db': review.book.pk,
            'user': review.user.username,
            'comment': review.comment,
            'created_at': datetime.fromisoformat(str(review.created_at)).strftime("%d-%m-%y %H:%M:%S"),
            'rating': review.rating, }
            for review in data_review]
    return JsonResponse(data,safe=False)
