from django.contrib import admin

from .models import Author, Book, BookItem


class BookItemInline(admin.TabularInline):
    model = BookItem
    fk_name = "title"


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "country"]
    fields = ['name', 'surname', "country"]
    search_fields = ["surname"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ["title", "price", "author"]
    list_filter = ["price"]
    inlines = [BookItemInline]


@admin.register(BookItem)
class BookItemAdmin(admin.ModelAdmin):
    fields = ["title", "isbn", "date_of_order"]
    list_filter = ["isbn"]
