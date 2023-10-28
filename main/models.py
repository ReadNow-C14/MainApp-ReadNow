from django.db import models
from book.models import Book

class HomePage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE) # one-to-many

    def __str__(self):
        return self.book.title  # book title as the string representation

    class Meta:
        verbose_name = "Homepage"
        verbose_name_plural = "Homepage"
