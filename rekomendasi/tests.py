from django.test import TestCase
from .views import *
from django.test import TestCase
from django.urls import reverse
from .models import Book, BookRecommendation

class YourAppTests(TestCase):
    def setUp(self):
        # Persiapan data yang diperlukan untuk pengujian
        self.book = Book.objects.create(
            title='Sample Book',
            authors='Sample Author',
            book_id = 12,
            publisher = "Publish Sample",
            isbn = "123123X",
        )

        self.book_recommendation = BookRecommendation.objects.create(
            recommended_book=self.book,
            source_book=self.book,
            recommendation_score=0.0,
        )

    def test_similar_books_view(self):
        response = self.client.get(reverse('rekomendasi:similar_books', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)

    def test_init_recommend_book(self):
        # Memastikan fungsi init_recommend_book bekerja sesuai harapan
        self.assertTrue(has_recommendations(self.book))

    def test_has_recommendations(self):
        # Memastikan fungsi has_recommendations mengembalikan True saat ada rekomendasi
        self.assertTrue(has_recommendations(self.book))

    def test_get_recommendations_json_view(self):
        response = self.client.get(reverse('rekomendasi:get_recommendations_json'))
        self.assertEqual(response.status_code, 200)

    def test_filter_books_ajax_view(self):
        response = self.client.get(reverse('rekomendasi:filter_books_ajax', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)

    def test_isbn_search_view(self):
        response = self.client.post(reverse('rekomendasi:isbn_search'), {'isbn': self.book.isbn})
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data.get('redirect_url'), reverse('rekomendasi:similar_books', args=[self.book.id]))
