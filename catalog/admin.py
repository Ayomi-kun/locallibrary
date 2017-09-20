from django.contrib import admin

# Register your models here.
#register each model here in the admin page
from .models import Author, Genre, Book, BookInstance

admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Author)