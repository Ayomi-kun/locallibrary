from django.db import models
# Create your models here.

class Genre(models.Model):
    """
    Model representating a book genre (e.g. Science Fiction, Non Fiction).
    """

    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Peotry etc.)")

    def __str__(self):
        """
        String for  representing the Model object (in Admin site etc.)
        """
        return self.name
        

from django.urls import reverse #used to generate URLS by reversing the URL patterns

class Book(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    #Authors as a string rather than an object because it hasent been decleared yet in the file.
    sumarry = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number </a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    #ManyToManyField used because genre can contain many books. Books can cover many genres.

    def __str__(self):
        """
        string for representating the Model object
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book-detail', args=[str(self.id)])