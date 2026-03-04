from django.contrib import admin
from .models import Author, Genre, Book, Reader, ReaderProfile, Loan


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'country', 'birth_year')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year', 'price', 'in_stock')
    list_filter = ('in_stock', 'author')
    filter_horizontal = ('genres',)


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email')


@admin.register(ReaderProfile)
class ReaderProfileAdmin(admin.ModelAdmin):
    list_display = ('reader', 'phone')


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('book', 'reader', 'loan_date', 'returned')
