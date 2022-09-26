from django.contrib import messages
from django.core.paginator import EmptyPage
from django.http import JsonResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.views import generic
from cart.forms import CartAddProductForm
from .forms import ContactForm, BookFilter
from .mixins import CacheMixin
from .models import Author, Book
from .tasks import contact_us
from django_filters.views import FilterView



def index(request):
    num_books = Book.objects.all().count()
    num_books_available = Book.objects.filter(available__exact=True).count()
    num_authors = Author.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_books': num_books,
                 'num_instances_available': num_books_available, 'num_authors': num_authors}, )


class SearchResultsListView(FilterView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'catalog/book_list.html'
    filterset_class = BookFilter


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


class AuthorListView(CacheMixin, generic.ListView):
    model = Author
    paginate_by = 5


class AuthorDetailView(CacheMixin, generic.DetailView):
    model = Author


def contact(request):
    data = dict()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data['form_is_valid'] = True
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            messages.add_message(request, messages.SUCCESS, 'Message was sent successfully!')
            contact_us.delay(subject, message, from_email)
            data['contact_form'] = render_to_string('base.html')
        else:
            data['form_is_valid'] = False
    else:
        form = ContactForm()
    context = {'form': form}
    data['html_form'] = render_to_string('catalog/contact.html', context, request=request)
    return JsonResponse(data)
