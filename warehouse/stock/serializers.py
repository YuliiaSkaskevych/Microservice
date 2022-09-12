from .models import Author, Publisher, BookInstance

from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name", "surname", "birth_date", "country"]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name", "price", "author"]


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ["publisher", "city"]


class BookInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = ["title", "publisher", "isbn", "date_of_order", "status"]
