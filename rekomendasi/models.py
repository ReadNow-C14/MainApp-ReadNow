from django.db import models
from book.models import Book

# Create your models here.
class BookRecommendation(models.Model):
    recommended_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    source_book = models.ForeignKey(Book, related_name='recommendations', on_delete=models.CASCADE)
    recommendation_score = models.IntegerField()

    def __str__(self):
        return f"Rekomendasi {self.recommended_book.title} dari {self.source_book.title}"