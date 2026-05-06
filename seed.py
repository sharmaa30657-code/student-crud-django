import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
django.setup()

from books.models import Book

books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "fiction", "year": 1925, "rating": 8.5, "description": "A story of wealth, ambition, and the American Dream set in the Jazz Age."},
    {"title": "Dune", "author": "Frank Herbert", "genre": "fantasy", "year": 1965, "rating": 9.2, "description": "An epic tale of politics, religion, and ecology on a desert planet."},
    {"title": "Sapiens", "author": "Yuval Noah Harari", "genre": "history", "year": 2011, "rating": 8.8, "description": "A sweeping history of the human species from stone age to the present."},
    {"title": "The Pragmatic Programmer", "author": "Andrew Hunt", "genre": "technology", "year": 1999, "rating": 9.0, "description": "Essential lessons for software developers on writing better code and building better habits."},
    {"title": "Gone Girl", "author": "Gillian Flynn", "genre": "mystery", "year": 2012, "rating": 8.1, "description": "A gripping psychological thriller about a marriage gone terrifyingly wrong."},
    {"title": "A Brief History of Time", "author": "Stephen Hawking", "genre": "science", "year": 1988, "rating": 9.1, "description": "Hawking's landmark exploration of cosmology, black holes, and the nature of time."},
]

Book.objects.all().delete()
for b in books:
    Book.objects.create(**b)

print(f"Seeded {len(books)} books.")
