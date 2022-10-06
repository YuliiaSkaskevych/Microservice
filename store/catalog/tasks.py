from celery import shared_task
import requests
from django.core.mail import send_mail as django_send_mail
from .models import Author, Book


@shared_task
def contact_us(subject, message, from_email):
    django_send_mail(subject, message, from_email, ['admin@example.com'])


@shared_task
def store_update():
    print('Starting update from warehouse api for database')
    print('Getting data from api...')
    url = 'http://warehouse:8000/authors/'
    print('Clearing data...')
    response_author = requests.get(url)
    if response_author.status_code != 200:
        return
    response_data_author = response_author.json()
    while True:
        for counter, data in enumerate(response_data_author['results']):
            Author.objects.update_or_create(
                id=data['id'],
                defaults={
                    'id': data['id'],
                    'name': data['name'],
                    'surname': data['surname'],
                    'country': data['country'],

                }
            )

        if response_data_author['next']:
            response_data_author = requests.get(response_data_author['next']).json()
        else:
            break

    url = 'http://warehouse:8000/books/'
    print('Clearing data...')
    response_book = requests.get(url)
    if response_book.status_code != 200:
        return
    response_data_book = response_book.json()
    while True:
        for counter, data in enumerate(response_data_book['results']):
            book, created = Book.objects.update_or_create(
                id=data['id'],
                defaults={
                    'id': data['id'],
                    "author": Author.objects.get(id=data['author']),
                    "title": data['title'],
                    "price": data['price'],
                    "rating": data['rating'],
                    "pubdate": data['pubdate'],
                    "available": data['available'],
                }
            )

            if not created:
                book.title = data['title']
                book.pubdate = data['pubdate']
                book.available = data['available']
                book.price = data['price']
                book.rating = data['rating']
                book.author = Author.objects.get(id=data['author'])
                book.save()
        if response_data_book['next']:
            response_data_book = requests.get(response_data_book['next']).json()
        else:
            break
    print('Database was updated from warehouse api')
