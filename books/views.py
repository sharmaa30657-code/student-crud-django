from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Book
from .forms import BookForm


def book_list(request):
    query = request.GET.get('q', '')
    genre = request.GET.get('genre', '')
    books = Book.objects.all()

    if query:
        books = books.filter(Q(title__icontains=query) | Q(author__icontains=query))
    if genre:
        books = books.filter(genre=genre)

    genre_choices = Book.GENRE_CHOICES
    context = {
        'books': books,
        'query': query,
        'selected_genre': genre,
        'genre_choices': genre_choices,
        'total': books.count(),
    }
    return render(request, 'books/book_list.html', context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'"{book.title}" has been added successfully!')
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form, 'action': 'Add New Book'})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, f'"{book.title}" has been updated!')
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form, 'book': book, 'action': 'Edit Book'})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        title = book.title
        book.delete()
        messages.success(request, f'"{title}" has been deleted.')
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})
