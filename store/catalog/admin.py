from django.contrib import admin

from .models import Author, Book


class BookInlineModelAdmin(admin.TabularInline):
    model = Book


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "country"]
    fields = ['name', 'surname', "country"]
    search_fields = ["surname"]
    inlines = [BookInlineModelAdmin]


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'author']
    fields = ['title', 'pubdate', 'author', ('price', 'pages')]
    raw_id_fields = ['author', ]
    date_hierarchy = "pubdate"
    list_filter = ['price', 'pubdate']
    search_fields = ["author", "title"]
