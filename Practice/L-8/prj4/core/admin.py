from django.contrib import admin

# Register your models here.
from .models import Book,Author,Publisher 

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name')

admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher','pub_date')

admin.site.register(Book,BookAdmin)

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','address','city')

admin.site.register(Publisher,PublisherAdmin)