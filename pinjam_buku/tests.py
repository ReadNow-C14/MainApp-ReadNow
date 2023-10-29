from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book, BorrowedBook

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
        self.borrowed_book = BorrowedBook.objects.create(user=self.user, book=self.book, return_date='2023-11-01')

    def test_borrow_book_ajax(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('borrow_book_ajax', args=[self.book.id]), {'return_date': '2023-11-15'})
        self.assertEqual(response.status_code, 201)
        self.book.refresh_from_db()
        self.assertEqual(self.book.status, 'Borrowed')

    def test_return_book_ajax(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('return_book_ajax', args=[self.book.id]))
        self.assertEqual(response.status_code, 201)
        self.book.refresh_from_db()
        self.assertEqual(self.book.status, 'Available')
