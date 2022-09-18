from celery import shared_task
import requests
from django.core.mail import send_mail as django_send_mail
from .models import Author, Book


@shared_task
def contact_us(subject, message, from_email):
    django_send_mail(subject, message, from_email, ['admin@example.com'])


@shared_task
def store_update():
    try:
        print('Starting update from warehouse api for database')  # noqa:T001
        print('Getting data from api...')
        url = 'http://warehouse:8001/authors/'
        print('Clearing data...')
        while url and (response_authors := requests.get(url)).status_code == requests.codes.ok:
            for author_data in response_authors.json()['results']:
                Author.objects.get_or_create(
                    id=author_data['id'],
                    defaults={
                        'name': author_data['name'],
                        'surname': author_data['surname'],
                        'country': author_data['country']

                    }
                )
            url = response_authors.json()['next']

        url = 'http://warehouse:8001/books/'
        print('Clearing data...')
        while url and (response_books := requests.get(url)).status_code == requests.codes.ok:
            for book_data in response_books.json()['results']:
                book, created = Book.objects.update_or_create(
                    isbn=book_data['isbn'],
                    defaults={
                        'id': book_data['id'],
                        "author": Author.objects.get(id=book_data['author']),
                        "title": book_data['title'],
                        "price": book_data['price'],
                        "pubdate": book_data['pubdate'],
                        "available": book_data['available'],
                        "rating": book_data['rating'],
                    }
                )

                url = response_books.json()['next']

    except Exception as e:
        print('Synchronization of two databases failed. See exception:')
        print(e)
    print('Database was updated from warehouse api')
