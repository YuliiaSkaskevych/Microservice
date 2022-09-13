import django_filters
from django.core.paginator import EmptyPage
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views import generic
from cart.forms import CartAddProductForm
from .mixins import CacheMixin
from .models import Author, Book


class ObjFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ["title", "author", "price", "rating", "available"]


def index(request):
    num_books = Book.objects.all().count()
    num_books_available = Book.objects.filter(available__exact=True).count()
    num_authors = Author.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_books': num_books,
                 'num_instances_available': num_books_available, 'num_authors': num_authors}, )


class BookListView(generic.ListView, CacheMixin):
    model = Book
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        filter = ObjFilter(self.request.GET, queryset)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        filter = ObjFilter(self.request.GET, queryset)
        context["filter"] = filter
        return context


def book_detail(request, pk):
    """Information about entered book: author, store, publisher"""
    try:
        book = get_object_or_404(Book, pk=pk)
        cart_product_form = CartAddProductForm()
        return render(
            request,
            'catalog/book_detail.html',
            {'book': book,
             'cart_product_form': cart_product_form,
             }
            )
    except EmptyPage:
        raise Http404


class AuthorListView(generic.ListView, CacheMixin):
    model = Author
    paginate_by = 5


class AuthorDetailView(generic.DetailView, CacheMixin):
    model = Author
