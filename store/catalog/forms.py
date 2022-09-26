from django import forms
import django_filters
from .models import Book
class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ["title", "author", "price", "rating", "available"]

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
