from django import forms
from .models import Book,Author,Publisher

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','pub_date','authors','publisher','rating','likes']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name','last_name','email']

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name','address','city','state_province','country','website']