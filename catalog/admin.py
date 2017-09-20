from django.contrib import admin

# Register your models here.
#register each model here in the admin page
from .models import Author, Genre, Book, BookInstance

#admin.site.register(Book)
#admin.site.register(BookInstance)
admin.site.register(Genre)
#admin.site.register(Author)

# doing an extended more detail and arranged look for our admin page

#define the Admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    # a way of neatly categorising the input details.
    fields = ['last_name', 'first_name', ('date_of_birth', 'date_of_death')]
#register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for Book using the decorator
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    
@admin.register(Book)
#note @admin.reister() does the same thing as admin.site.register
class BookAdmin(admin.ModelAdmin):
    #genre cannot be called in the below tuples because genre is a many to many field
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_display= ('book', 'status', 'due_back', 'id')
    list_filter= ('book', 'status', 'due_back', 'id')

    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )