from django.urls import path
from .views import BookListView, AuthorListView, AuthorDetailView, book_detail, index


urlpatterns = [
    path('', index, name='index'),
    path('books/', BookListView.as_view(), name='books'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>', AuthorDetailView.as_view(), name='author_detail'),
    path('books/<int:pk>', book_detail, name='book_detail'),
]
