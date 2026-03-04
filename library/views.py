from django.shortcuts import render, get_object_or_404
from .models import Book, Author, Reader


def books_list(request):
    books = Book.objects.all().select_related('author').prefetch_related('genres')
    return render(request, 'library/books_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(
        Book.objects.select_related('author').prefetch_related('genres', 'loans__reader'),
        pk=pk
    )
    return render(request, 'library/book_detail.html', {'book': book})


def authors_list(request):
    authors = Author.objects.all().prefetch_related('books')
    return render(request, 'library/authors_list.html', {'authors': authors})


def author_detail(request, pk):
    author = get_object_or_404(
        Author.objects.prefetch_related('books'),
        pk=pk
    )
    return render(request, 'library/author_detail.html', {'author': author})


def readers_list(request):
    readers = Reader.objects.all().select_related('profile').prefetch_related('loans__book')
    return render(request, 'library/readers_list.html', {'readers': readers})


def reader_detail(request, pk):
    reader = get_object_or_404(
        Reader.objects.select_related('profile').prefetch_related('loans__book'),
        pk=pk
    )
    return render(request, 'library/reader_detail.html', {'reader': reader})
