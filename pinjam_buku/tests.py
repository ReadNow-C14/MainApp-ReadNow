from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book, BorrowedBook
from datetime import datetime

class BorrowBookTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.book = Book.objects.create(
            title='Sample Book',
            authors='Sample Author',
            book_id = 12,
            publisher = "Publish Sample",
            isbn = "123123X",
            status = "Available"
        )
        self.borrowed_book = BorrowedBook.objects.create(user=self.user, book=self.book, return_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f%z"))

    def test_borrow_book_ajax(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('pinjam_buku:borrow_book_ajax', args=[self.book.id]), {'return_date': datetime.now().strftime("%Y-%m-%d")})
        self.assertEqual(response.status_code, 201)
        self.book.refresh_from_db()
        self.assertEqual(self.book.status, 'Borrowed')

    def test_return_book_ajax(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('pinjam_buku:return_book_ajax', args=[self.book.id]))
        self.assertEqual(response.status_code, 201)
        self.book.refresh_from_db()
        self.assertEqual(self.book.status, 'Available')
