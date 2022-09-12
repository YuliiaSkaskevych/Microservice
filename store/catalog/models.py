from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    birthdate = models.DateField()
    deathdate = models.DateField()

    def __str__(self):
        return f"{self.name} {self.surname}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pubdate = models.DateField(auto_now_add=True)
    rating = models.FloatField('Rating')
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} | {self.price} | {self.author}"
