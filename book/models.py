from django.db import models

# Create your models here.
class Book(models.Model):
    book_id = models.IntegerField(null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length = 255)
    num_of_pages = models.IntegerField(null=True, blank=True)
    language = models.CharField(null=True, blank=True, max_length = 255)
    authors = models.CharField(null=True, blank=True, max_length = 255)
    publisher = models.CharField(null=True, blank=True, max_length = 255)
    isbn = models.CharField(null=True, blank=True, max_length = 255)
    counts_of_review = models.IntegerField(null=True, blank=True)
    rating_dist_total = models.IntegerField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    rating_dist1 = models.IntegerField(null=True, blank=True)
    rating_dist2 = models.IntegerField(null=True, blank=True)
    rating_dist3 = models.IntegerField(null=True, blank=True)
    rating_dist4 = models.IntegerField(null=True, blank=True)
    rating_dist5 = models.IntegerField(null=True, blank=True)
    indices = models.CharField(null=True, blank=True, max_length = 700)
    distance =  models.CharField(null=True, blank=True, max_length = 700)
    image_url = models.URLField(null=True, blank=True)
    small_image_url = models.URLField(null=True, blank=True)
    publish_day = models.IntegerField(null=True, blank=True)
    publish_month = models.IntegerField(null=True, blank=True)
    publish_year = models.IntegerField(null=True, blank=True)

    def get_indices_as_list(self):
        # Memisahkan string berdasarkan koma dan mengonversi ke integer
        return [int(index) for index in self.indices.split(',')]
    
    def get_distances_as_list(self):
        # Memisahkan string berdasarkan koma dan mengonversi ke integer
        return [float(index) for index in self.distance.split(',')]