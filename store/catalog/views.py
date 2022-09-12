from django.shortcuts import render
from django.views import generic


from .models import Author, Book


def index(request):
    num_books = Book.objects.all().count()
    num_books_available = Book.objects.filter(status__exact='available').count()
    num_authors = Author.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_books': num_books,
                 'num_instances_available': num_books_available, 'num_authors': num_authors},)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 20


def book_detail(request, id):
    """Information about entered book: author, store, publisher"""
    book = Book.objects.select_related('author').get(id=id)
    return render(
        request,
        'catalog/book_info.html',
        {'id': book.id,
         'title': book.title,
         'pages': book.pages,
         'price': book.price,
         'pubdate': book.pubdate,
         'author': book.author.surname,
         'author_id': book.author.id,
         }
    )


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 20


class AuthorDetailView(generic.DetailView):
    model = Author
