from django.contrib import admin

from .models import Author, Book, BookInstance, Publisher


class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    fk_name = "title"
    fk_name2 = "publisher"


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "country"]
    fields = ['name', 'surname', "country"]
    search_fields = ["surname"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ["title", "price", "author"]
    list_filter = ["price"]
    inlines = [BookInstanceInline]


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    fields = ["publisher", "city"]
    list_filter = ["publisher"]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    fields = ["title", "isbn", "publisher", "date_of_order", "status"]
    list_filter = ["isbn"]
