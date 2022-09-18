from .models import Author, BookItem, Book

from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name", "surname", "country"]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title", "price", "author"]


class BookItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookItem
        fields = ["title", "isbn", "date_of_order"]
