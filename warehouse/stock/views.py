from .permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from .models import Author, Book, BookItem
from .serializers import AuthorSerializer, BookSerializer, BookItemSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsOwnerOrReadOnly]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrReadOnly]

class BookInstanceViewSet(viewsets.ModelViewSet):
    queryset = BookItem.objects.all()
    serializer_class = BookItemSerializer
    permission_classes = [IsOwnerOrReadOnly]
