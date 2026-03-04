from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_list, name='books_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('authors/', views.authors_list, name='authors_list'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('readers/', views.readers_list, name='readers_list'),
    path('reader/<int:pk>/', views.reader_detail, name='reader_detail'),
]
