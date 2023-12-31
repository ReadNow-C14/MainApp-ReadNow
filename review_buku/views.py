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
import json


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
            reviews = Review.objects.get(
                user__id=request.user.id, book__id=book_id)
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
    if request.method == 'POST':
        try:
            reviews = Review.objects.get(
                user__id=request.user.id, book__id=book_id)
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
    book = Book.objects.get(pk=book_id)
    data_review = Review.objects.filter(book=book)
    data = [{'book': review.book.pk,
            'user': review.user.username,
             'comment': review.comment,
             'created_at': datetime.fromisoformat(str(review.created_at)).strftime("%d-%m-%y %H:%M:%S"),
             'rating': review.rating, }
            for review in data_review]
    return JsonResponse(data, safe=False)


# def submit_review_flutter(request, book_id):
#     if request.method == 'POST':
#         # Anda mungkin perlu menyesuaikan bagian ini untuk deserialisasi JSON
#         data = json.loads(request.body)

#         try:
#             # Jika Anda menggunakan `request.user`, pastikan request tersebut sudah memiliki user yang terautentikasi
#             reviews = Review.objects.get(user=request.user.id, book__id=book_id)
#             form = ReviewForm(request.POST, instance=reviews)
#         except Review.DoesNotExist:
#             form = ReviewForm(request.POST)

#         if form.is_valid():
#             review = form.save(commit=False)
#             review.user = request.user
#             review.book_id = book_id
#             review.save()

#             # Mengembalikan JsonResponse dengan status 'created'
#             return JsonResponse({'status': 'success', 'message': 'Review created successfully'}, status=201)
#         else:
#             # Mengembalikan JsonResponse dengan pesan error
#             return JsonResponse({'status': 'error', 'message': 'There was an error with your submission'}, status=400)
#     else:
#         # Metode HTTP tidak diizinkan
#         return JsonResponse({'status': 'error', 'message': 'HTTP method not allowed'}, status=405)
@csrf_exempt
def submit_review_flutter(request, book_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_product = Review.objects.create(
            user = request.user,
            book = Book.objects.get(pk=data["book"]),
            rating = int(data["rating"]),
            comment = data["comment"],
            created_at = datetime.now()
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

