from django.shortcuts import render, redirect
from .forms import AuthorForm, PublisherForm, BookForm
from .models import Author,Publisher,Book


def index(request):
    return render(request, 'index.html')

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_create')
    else:
        form = AuthorForm()
    return render(request, 'author_create.html', {'form': form})

# Similarly, define views for Publisher and Book creation


def publisher_create(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publisher_create')
    else:
        form = PublisherForm()
    return render(request, 'publisher_create.html', {'form': form})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_create')
    else:
        form = BookForm()
    return render(request, 'book_create.html', {'form': form})



def display_all(request):
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    books = Book.objects.all()
    return render(request, 'display_all.html', {'authors': authors, 'publishers': publishers, 'books': books})

