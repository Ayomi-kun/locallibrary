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