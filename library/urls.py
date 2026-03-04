from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_list, name='books_list'),
    path('authors/', views.authors_list, name='authors_list'),
    path('readers/', views.readers_list, name='readers_list'),
]
