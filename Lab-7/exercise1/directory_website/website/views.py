from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoryForm, PageForm
from .models import Category, Page

def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})

def add_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.save()
            # Increment visits count for the associated category
            page.category.visits += 1
            page.category.save()
            return redirect('home')
    else:
        form = PageForm()
    return render(request, 'add_page.html', {'form': form})

def like_page(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    page.likes += 1
    page.save()
    return redirect('home')

def visit_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    category.visits += 1
    category.save()
    return redirect('home')
