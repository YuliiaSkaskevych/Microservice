from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    country = models.CharField(max_length=500)

    class Meta:
        unique_together = ['name', 'surname']

    def str(self):
        return f'{self.name} {self.surname}'


class Book(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pubdate = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField('Rating')
    available = models.BooleanField(default=True)

    def _str_(self):
        return self.title


class Publisher(models.Model):
    publisher = models.CharField('Publisher', max_length=200)
    city = models.CharField('City', max_length=100)


class BookInstance(models.Model):

    IN_PROGRESS = 'In_progress'
    PACKED = 'Packed'
    DELIVERING = 'Delivering'
    RECEIVED = 'Received'

    CHOICE_STATUS = {
        (IN_PROGRESS, 'In_progress'),
        (PACKED, 'Packed'),
        (DELIVERING, 'Delivering'),
        (RECEIVED, 'Received')
    }

    title = models.ForeignKey(Book, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    date_of_order = models.DateTimeField(auto_now_add=True)
    status = models.CharField('Status', choices=CHOICE_STATUS, max_length=30, default=IN_PROGRESS)

    def __str__(self):
        return f'{self.isbn} + {self.status}'
