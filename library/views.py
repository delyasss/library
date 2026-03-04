from django.shortcuts import render
from .models import Book


def books_list(request):
    """Задание 5: все книги + связанные автор и жанры (обратные связи)."""
    books = Book.objects.all().select_related('author').prefetch_related('genres')
    return render(request, 'library/books_list.html', {'books': books})
