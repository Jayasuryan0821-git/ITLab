from django.shortcuts import render,redirect
from .models import Author,Book,Publisher
from .forms import AuthorForm,BookForm,PublisherForm
# Create your views here.
def index(request):
    return render(request,'index.html')

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AuthorForm()
    return render(request,'author_create.html',{'form':form})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_all')
    else:
        form = BookForm()
    return render(request,'book_create.html',{'form':form})

def publisher_create(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_all')
    else:
        form = PublisherForm()
    return render(request,'publisher_create.html',{'form':form}) 
 
def display_all(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    return render(request,'display_all.html',{'books':books,'authors':authors,'publishers':publishers})
