from django.shortcuts import render
from .models import Book, Author, Reader


def books_list(request):
    books = Book.objects.all().select_related('author').prefetch_related('genres')
    return render(request, 'library/books_list.html', {'books': books})


def authors_list(request):
    authors = Author.objects.all().prefetch_related('books')
    return render(request, 'library/authors_list.html', {'authors': authors})


def readers_list(request):
    readers = Reader.objects.all().select_related('profile').prefetch_related('loans__book')
    return render(request, 'library/readers_list.html', {'readers': readers})
