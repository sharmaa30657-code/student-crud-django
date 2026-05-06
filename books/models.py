from django.db import models


class Book(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non-Fiction'),
        ('science', 'Science'),
        ('history', 'History'),
        ('biography', 'Biography'),
        ('technology', 'Technology'),
        ('fantasy', 'Fantasy'),
        ('mystery', 'Mystery'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, default='fiction')
    year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} by {self.author}"
