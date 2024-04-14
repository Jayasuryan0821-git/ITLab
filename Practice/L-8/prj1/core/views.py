from django.shortcuts import render,redirect
from .models import Page,Category
from .forms import CategoryForm,PageForm
# Create your views here.

def index(request):
    categories = Category.objects.all()
    return render(request,'index.html',{'categories':categories})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Make sure 'index' is a valid URL pattern name in your urls.py
    else:
        form = CategoryForm()  # This ensures form is always initialized for GET requests

    return render(request, 'add_category.html', {'form': form})

    
def add_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PageForm()
    return render(request,'add_page.html',{'form':form}) 
 