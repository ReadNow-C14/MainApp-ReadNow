from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, JsonResponse
from django.core import serializers
from book.models import Book
from .models import BookRecommendation
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def similar_books(request, id):
    book = Book.objects.get(pk = id)

    # Periksa apakah rekomendasi sudah ada
    if not has_recommendations(book):
        init_recommend_book(book)

    selected_publish_year = request.GET.get('publishYear')
    recommendation_books = BookRecommendation.objects.filter(source_book=book)

    if selected_publish_year:
        # Jika tahun penerbitan sudah ada dalam request, maka filter berdasarkan tahun
        recommendation_books = recommendation_books.filter(
            recommended_book__publish_year=selected_publish_year
        )

    context = {"main_book" : book,
               'recommendation_books': recommendation_books}
    return render(request, 'similar_books.html', context)

def init_recommend_book(source_book):
    # Dapatkan buku-buku lain oleh penulis yang sama
    recommended_books = [Book.objects.get(pk = i+1) for i in source_book.get_indices_as_list()[1:]]
    distance = [int(i) for i in source_book.get_distances_as_list()[1:]]

    for index, recommended_book in enumerate(recommended_books):
        recommendation_score = distance[index]
        # Buat objek BookRecommendation
        recommendation = BookRecommendation(
            recommended_book=recommended_book,
            source_book=source_book,
            recommendation_score=recommendation_score,
        )

        # Simpan objek BookRecommendation ke dalam database
        recommendation.save()

def has_recommendations(source_book):
    # Periksa apakah ada BookRecommendation yang sudah terkait dengan source_book
    return BookRecommendation.objects.filter(source_book=source_book).exists()

def get_recommendations_json(request):
    data = BookRecommendation.objects.all()
    return HttpResponse(serializers.serialize("json",data),content_type="application/json")

@csrf_exempt
def filter_books_ajax(request, id):
    book = Book.objects.get(pk = id)

    # Periksa apakah rekomendasi sudah ada
    if not has_recommendations(book):
        init_recommend_book(book)

    selected_publish_year = request.GET.get('publishYear')
    recommendation_books = BookRecommendation.objects.filter(source_book=book)

    if selected_publish_year:
        # Jika tahun penerbitan sudah ada dalam request, maka filter berdasarkan tahun
        recommendation_books = recommendation_books.filter(
            recommended_book__publish_year=selected_publish_year
        )

    # NOTE: Masih perlu diatur tergantung kebutuhan pas di similar_book.html nantinya
    data = [{'title': rec.recommended_book.title, 'authors': rec.recommended_book.authors, 'rating': rec.recommended_book.rating, 'image_url': rec.recommended_book.image_url} for rec in recommendation_books]

    return JsonResponse(data, safe=False)


@csrf_exempt
def isbn_search(request):
    if request.method == 'POST':
        isbn = request.POST.get('isbn')
        try:
            book = Book.objects.get(isbn=isbn)  # Replace with the actual model and field name
            # Use reverse to get the URL for the 'similar_books' view
            url = reverse('rekomendasi:similar_books', args=[book.id])
            # Create a JSON response with the redirect URL
            response_data = {'redirect_url': url}
            return JsonResponse(response_data)
        except Book.DoesNotExist:
            return JsonResponse({'error': 'ISBN not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)

